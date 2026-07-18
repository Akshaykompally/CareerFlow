import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from typing import TypedDict
from interview_details import get_interviews
from langgraph.graph import StateGraph, START, END
from extensions import mysql
import markdown
import re


class State(TypedDict):
    Interview_details : str
    Interview_status  : str
    Mistakes_focus    : str
    Need_to_focus     : str
    Study_plan        : str


load_dotenv()


api_key = os.getenv("HuggingFaceHub_API_Token")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

def Mistakes_focus(state:State) -> dict:
    status = state["Interview_status"].strip().lower()
    
    print("-> 🤞🤞🤞 The Mistakes need to focus !!! 🤞🤞🤞")

    if status == "selected":
        prompt = ( f"""
            You are a senior interview coach.

            The candidate has successfully cleared the interview.

            Interview Details:
            {state["Interview_details"]}

            Do NOT identify mistakes.

            Instead return:

            ## Interview Result
            Accepted

            ## Strengths
            - Exactly 2 strengths with brief explanations.

            ## Growth Opportunities
            - Exactly 2 minor improvement opportunities.

            ## Career Recommendations
            - Exactly 2 recommendations for future interviews.

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
            """
            )
    elif status == "pending":
        prompt = ( f"""
            You are a senior interview coach.

            The interview result is still pending.

            Interview Details:
            {state["Interview_details"]}

            Return:

            ## Current Assessment
            - Short assessment

            ## Strengths
            - Exactly 2 points

            ## Possible Improvements
            - Exactly 2 points

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
            """
            )
    else:
        prompt = (
            f"""
                You are a senior technical interview coach with over 15 years of experience evaluating software engineering candidates.

                Your task is to carefully analyze the interview transcript and identify the candidate's most significant performance issues.

                Interview Details:
                {state["Interview_details"]}

                Instructions:
                - Read the complete interview before making conclusions.
                - Base every observation only on the interview content.
                - Prioritize the issues that had the greatest negative impact.
                - Do not repeat the same issue across different sections.
                - Every point should clearly describe:
                • What the issue was.
                • Why it affected the interview.
                - Each point should contain 10 words (approximately one line).
                - Keep the language professional, constructive, and specific.
                - Do not provide solutions in this section.

                Return ONLY the following format:

                ## Mistakes
                - Exactly 2 important mistakes.

                ## Weak Areas
                - Exactly 2 skill gaps or weaknesses.

                Return only the formatted response.
                Formatting Rules:
                - Do not insert blank lines between headings and bullet points.
                - Do not insert blank lines between bullet points.
                - Keep the response compact.
                """
            )
    print("-> 📞📞📞 Calling  LLM Groq 📞📞📞")
    response = model.invoke(prompt)
    print("-> 🥳🥳🥳 LLM Return the response scucessfully 🥳🥳🥳")
    return {"Mistakes_focus" : response.content.strip()}


def Need_to_focus(state:State) -> dict:
    
    status = state["Interview_status"].strip().lower()

    
    if status == "selected":
        prompt = (f"""
            The candidate has cleared the interview.

            Based on:

            {state["Mistakes_focus"]}

            Return:

            ## Advanced Skills
            - Exactly 2 skills to learn next.

            ## Career Tips
            - Exactly 2 professional growth tips.

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
            """
        )
    elif status == "pending":
        prompt = (f"""
            The interview is pending.

            Based on:

            {state["Mistakes_focus"]}

            Return:

            ## Next Round Focus
            - Exactly 2 preparation topics.

            ## Preparation Tips
            - Exactly 2 practical tips.

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
            """
        )
    else:
        prompt = (
        f"""
            You are an expert interview mentor.

            Based on the interview analysis below, determine the highest-priority areas the candidate should improve before attending another technical interview.

            Interview Analysis:
            {state["Mistakes_focus"]}

            Instructions:
            - Prioritize improvements that will have the greatest impact.
            - Focus on knowledge, communication, confidence, and interview strategy where appropriate.
            - Do not repeat similar recommendations.
            - Every topic should include a short explanation.
            - Every preparation tip should be practical and immediately actionable.
            - Each point should contain 10 words (approximately one lines).
            - Avoid generic advice such as "practice more" or "study harder."

            Return ONLY this format:

            ## Topics to Improve
            - Exactly 2 topics with a brief explanation.

            ## Preparation Tips
            - Exactly 2 practical interview-focused tips.

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
            """
        )

    response = model.invoke(prompt)
    return {"Need_to_focus" : response.content.strip()}


def Study_plan(state:State) -> dict:

    status = state["Interview_status"].strip().lower()

    if status == "selected":
        prompt = (f"""
            The candidate successfully cleared the interview.

            Based on:

            {state["Need_to_focus"]}

            Return:

            ## Next Learning Goals
            - Exactly 2 advanced technical topics.

            ## Career Development
            - Exactly 2 recommendations for becoming a stronger software engineer.

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
            """
        )
    elif status == "pending":
        prompt = (f"""
        The interview result is pending.

        Based on:

        {state["Need_to_focus"]}

        Return:

        ## Next Round Preparation
        - Exactly 2 topics.

        ## Preparation Strategy
        - Exactly 2 tips.

        Return only the formatted response.
        Formatting Rules:
        - Do not insert blank lines between headings and bullet points.
        - Do not insert blank lines between bullet points.
        - Keep the response compact.
        """
        )
    else:
        prompt = (
        f"""
            You are a senior software engineering interview mentor.

            Create a personalized study plan based on the candidate's improvement areas.

            Improvement Areas:
            {state["Need_to_focus"]}

            Instructions:
            - Recommend the three most important topics the candidate should study first.
            - Explain why each topic is important.
            - Suggest preparation techniques that directly improve interview performance.
            - Recommendations should be practical, specific, and achievable.
            - Avoid generic advice.
            - Each point should contain 10 words (approximately one lines).
            - Keep the plan concise but actionable.

            Return ONLY this format:

            ## Topics to Study
            - Exactly 2 study topics with a short explanation.

            ## Preparation Tips
            - Exactly 2 actionable preparation tips.

            Return only the formatted response.
            Formatting Rules:
            - Do not insert blank lines between headings and bullet points.
            - Do not insert blank lines between bullet points.
            - Keep the response compact.
        """
    )

    response = model.invoke(prompt)
    return {"Study_plan" : response.content.strip()}


graph = StateGraph(State)

graph.add_node("mistakes",Mistakes_focus)
graph.add_node("next_time_to_focus",Need_to_focus)
graph.add_node("plan",Study_plan)


graph.add_edge(START,"mistakes")
graph.add_edge("mistakes","next_time_to_focus")
graph.add_edge("next_time_to_focus","plan")
graph.add_edge("plan",END)


print("-> ⌛⌛⌛ Compiling graph ⌛⌛⌛ ")

app = graph.compile()

def clean_html(text):

    # Remove extra blank lines
    text = re.sub(r'\n\s*\n+', '\n', text)

    # Convert markdown to HTML
    html = markdown.markdown(text)

    return html


def analyze_all_interviews():

    # interviews = get_interviews()

    analysis = []

    for interview in interviews:

        details = f"""
        Company         : {interview[1]}
        Role            : {interview[2]}
        Date            : {interview[3]}
        Status          : {interview[4]}
        Rounds Attended : {interview[5]}
        Feedback        : {interview[6]}
        """

        cursor = mysql.connection.cursor()

        cursor.execute("""
        SELECT
            ai_generated,
            ai_mistakes,
            ai_focus,
            ai_study_plan
        FROM interview_details
        WHERE id=%s
        """, (interview[0],))

        ai = cursor.fetchone()

        if ai and ai[0]:

            result = {
                "Mistakes_focus": ai[1],
                "Need_to_focus": ai[2],
                "Study_plan": ai[3]
            }

        else:

            result = app.invoke({
                "Interview_details": details,
                "Interview_status": interview[4]
            })

            cursor.execute("""
            UPDATE interview_details
            SET
                ai_mistakes=%s,
                ai_focus=%s,
                ai_study_plan=%s,
                ai_generated=TRUE
            WHERE id=%s
            """,
            (
                result["Mistakes_focus"],
                result["Need_to_focus"],
                result["Study_plan"],
                interview[0]
            ))

            mysql.connection.commit()

        analysis.append({

            "company": interview[1],

            "role": interview[2],

            "status": interview[4],

            "mistakes": clean_html(result["Mistakes_focus"]),

            "focus": clean_html(result["Need_to_focus"]),

            "study": clean_html(result["Study_plan"])

        })

    return analysis

print("-> 🏁🏁🏁 Graph finished 🏁🏁🏁")



