from flask import Blueprint, render_template
from flask_login import login_required, current_user
from extensions import mysql

history = Blueprint("history", __name__)

@history.route("/History")
@login_required
def history_page():

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM interview_details
        WHERE user_id=%s
        ORDER BY date_attended DESC
        """,
        (current_user.id,)
    )

    result = cursor.fetchall()

    cursor.execute(
        """
        SELECT status_of_interview, COUNT(*)
        FROM interview_details
        WHERE user_id=%s
        GROUP BY status_of_interview
        """,
        (current_user.id,)
    )

    values_count = cursor.fetchall()

    cursor.close()

    data = [row[1] for row in values_count]
    n_interviews = sum(data)

    return render_template(
        "History.html",
        result=result,
        n_interviews=n_interviews
    )