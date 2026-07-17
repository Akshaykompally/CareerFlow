from flask_login import current_user
from extensions import mysql


def get_interviews():
    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM interview_details WHERE user_id=%s",
        (current_user.id,)
    )

    interviews = cursor.fetchall()
    cursor.close()

    return interviews