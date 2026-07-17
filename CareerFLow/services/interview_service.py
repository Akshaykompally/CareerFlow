
from extensions import mysql

def save_interview(user_id, company, role, date, status, rounds, notes):
    cursor = mysql.connection.cursor()
    cursor.execute(
        """
        INSERT INTO interview_details
        (user_id, company_name, applied_role, date_attended,
         status_of_interview, no_of_rounds_attended, fingure_it_out)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (user_id, company, role, date, status, rounds, notes),
    )
    mysql.connection.commit()
    cursor.close()