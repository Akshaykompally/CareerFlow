from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

mysql = MySQL()

login_manager = LoginManager()

bcrypt = Bcrypt()