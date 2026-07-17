from flask_login import UserMixin
from extensions import mysql


class User(UserMixin):
    def __init__(self,user_id,full_name,user_email,user_password):
        self.id = user_id
        self.first = full_name
        self.email = user_email
        self.password = user_password

    @staticmethod
    def get(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT full_name,user_email,user_password FROM login_credits WHERE user_id = %s',(user_id,))
        res = cursor.fetchone()
        cursor.close()
        if res:
            return User(user_id,res[0],res[1],res[2])
        return None
