from flask import Blueprint, render_template
from flask_login import login_required, current_user
from extensions import mysql
from collections import Counter

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/Dashboard")
@login_required
def dashboard_page():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM interview_details WHERE user_id=%s",
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

    labels = [row[0] for row in values_count]
    data = [row[1] for row in values_count]

    n_interviews = sum(data)

    accept = 0
    reject = 0
    pending = 0

    for status, count in values_count:
        if status == "Selected":
            accept = count
        elif status == "Rejected":
            reject = count
        elif status == "Pending":
            pending = count

    rounds_list = []

    for row in result:
        if row[5]:
            rounds = row[5].split(",")
            rounds_list.extend(rounds)

    round_counts = Counter(rounds_list)

    round_labels = list(round_counts.keys())
    round_data = list(round_counts.values())

    return render_template(
        "Dashboard.html",
        username=current_user.first,
        result=result,
        labels=labels,
        data=data,
        round_labels=round_labels,
        round_data=round_data,
        n_interviews=n_interviews,
        accept=accept,
        reject=reject,
        pending=pending,
    )