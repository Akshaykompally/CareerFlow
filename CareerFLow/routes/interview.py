from flask import Blueprint, render_template,render_template, request, redirect, url_for, flash
from flask_login import login_required ,current_user
from extensions import mysql

interview = Blueprint("interview", __name__)

@interview.route("/AddInterview", methods = ["POST","GET"])
@login_required
def add_interview():
    if request.method == "POST":

        company_name = request.form["company-name"]
        applied_role = request.form["role"]
        date_attended = request.form["date"]
        status_of_interview = request.form["status"]

        no_of_rounds_attended = request.form.getlist("choice")
        no_of_rounds_attended = ",".join(no_of_rounds_attended)

        fingure_it_out = request.form["notes"]

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            INSERT INTO interview_details
            (
                user_id,
                company_name,
                applied_role,
                date_attended,
                status_of_interview,
                no_of_rounds_attended,
                fingure_it_out,
                ai_generated
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,FALSE)
            """,
            (
                current_user.id,
                company_name,
                applied_role,
                date_attended,
                status_of_interview,
                no_of_rounds_attended,
                fingure_it_out,
            ),
        )

        mysql.connection.commit()
        cursor.close()

        flash("Interview added successfully!", "success")
        return redirect(url_for("dashboard.dashboard_page"))

    return render_template("Add_Interview.html")

@interview.route("/delete/<int:id>")
@login_required
def delete_interview(id):

    print("Deleting Interview ID:", id)

    cursor = mysql.connection.cursor()

    cursor.execute("""
        DELETE FROM interview_details
        WHERE id=%s AND user_id=%s
    """, (id, current_user.id))

    print("Rows Deleted:", cursor.rowcount)

    mysql.connection.commit()
    cursor.close()

    flash("Interview deleted successfully!", "success")

    return redirect(url_for("history.history_page"))