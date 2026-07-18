from flask import Flask
from routes.auth import auth
from config import Config
from routes.history import history
from routes.interview import interview
from routes.dashboard import dashboard
from routes.ai import ai
from extensions import mysql, login_manager, bcrypt

app = Flask(__name__)

app.config.from_object(Config)

mysql.init_app(app)

login_manager.init_app(app)

bcrypt.init_app(app)

app.register_blueprint(auth)


app.register_blueprint(dashboard)

app.register_blueprint(interview)

app.register_blueprint(history)

app.register_blueprint(ai)

print(app.url_map)

@app.route("/")
def home():
    return "CareerFlow is running successfully!"