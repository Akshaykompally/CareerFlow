from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from extensions import mysql, bcrypt, login_manager
from models import User

auth = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



@auth.route('/')
def home():
    return render_template('Hero.html')


@auth.route('/Login', methods = ['POST','GET'])
def login_page():
    if request.method == 'POST':

        user_email = request.form['email']
        user_password = request.form['password']

        cursor = mysql.connection.cursor()

        cursor.execute('SELECT user_id,full_name,user_email,user_password FROM login_credits WHERE user_email=%s',(user_email,))
        user_data = cursor.fetchone()
        cursor.close()

        if user_data and bcrypt.check_password_hash(user_data[3],user_password):
            user = User(user_data[0],user_data[1],user_data[2],user_data[3])
            login_user(user)
    
            print("Current User ID:", user.id, flush=True)
            flash("✅ Welcome back", "success")
            return redirect(url_for("dashboard.dashboard_page"))
        else:
            flash("❌ Invalid Email or Password","error")
    return render_template('Login.html')


@auth.route('/Signup', methods = ['POST','GET'])
def signup_page():
    if request.method == 'POST':
        full_name = request.form['fname']
        user_email = request.form['email']
        user_password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(user_password).decode('utf-8')
        
        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT user_id FROM login_credits WHERE user_email = %s",
            (user_email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            flash("❌ Email already exists","error")
            cursor.close()
            return redirect(url_for('auth.signup_page'))


        cursor.execute(
            """
            INSERT INTO login_credits
            (full_name, user_email, user_password)
            VALUES (%s, %s, %s)
            """,
            (full_name, user_email, hashed_password)
        )

        mysql.connection.commit()
        cursor.close()

        flash("✅ Signup successful. Please login.","success")
        return redirect(url_for('auth.login_page'))

    return render_template('Signup.html')


@auth.route("/logout")
def logout():
    logout_user()
    flash(" ✅ Logged out successfully.", "success")
    return redirect(url_for("auth.login_page"))