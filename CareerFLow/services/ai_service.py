from interview_details import get_interviews
from Analyze_interviews import app
from markdown import markdown
from extensions import mysql


def analyze_all_interviews():

    interviews = get_interviews()

    analysis = []

    cursor = mysql.connection.cursor()

    for interview in interviews:

        interview_id = interview[0]

        # If AI is already generated, use cached data
        if interview[11]:

            analysis.append({

                "company": interview[1],
                "role": interview[2],
                "status": interview[4],
                "mistakes": interview[8],
                "focus": interview[9],
                "study": interview[10]

            })

            continue

        details = f"""
Company         : {interview[1]}
Role            : {interview[2]}
Date            : {interview[3]}
Status          : {interview[4]}
Rounds Attended : {interview[5]}
Feedback        : {interview[6]}
"""

        result = app.invoke({

            "Interview_details": details,
            "Interview_status": interview[4]

        })

        mistakes = markdown(result["Mistakes_focus"])
        focus = markdown(result["Need_to_focus"])
        study = markdown(result["Study_plan"])

        cursor.execute(
            """
            UPDATE interview_details
            SET
                ai_mistakes=%s,
                ai_focus=%s,
                ai_study_plan=%s,
                ai_generated=TRUE
            WHERE id=%s
            """,
            (
                mistakes,
                focus,
                study,
                interview_id
            )
        )

        mysql.connection.commit()

        analysis.append({

            "company": interview[1],
            "role": interview[2],
            "status": interview[4],
            "mistakes": mistakes,
            "focus": focus,
            "study": study

        })

    cursor.close()

    return analysis