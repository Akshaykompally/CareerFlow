from flask import Blueprint, render_template
from flask_login import login_required
from services.ai_service import analyze_all_interviews

ai = Blueprint("ai", __name__)

@ai.route("/AI_Insights")
@login_required
def ai_insights():
    analysis = analyze_all_interviews()
    return render_template("AI.html", analysis=analysis)