import os
import mysql.connector
from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
import bcrypt
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db_connection():
    connection = mysql.connector.connect(
        user='root',
        password='1234567',
        host='localhost',
        database='practice_20240917',
        auth_plugin='mysql_native_password'
    )
    return connection

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")
    
    def validate_email(self, field):
        # Verify email format
        try:
            v = validate_email(field.data)
        except EmailNotValidError as e:
            raise ValidationError(str(e))
        
        # Check if email already exists
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM new_users WHERE email=%s", (field.data,))
            user = cursor.fetchone()
        finally:
            cursor.close()
            connection.close()
        
        if user:
            raise ValidationError('Email is already taken')

class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()]) 
    submit = SubmitField("Login")

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO new_users (name, email, password) VALUES (%s, %s, %s)", 
                           (name, email, hashed_password.decode('utf-8')))
            connection.commit()
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM new_users WHERE name=%s", (name,))
            user = cursor.fetchone()
        except mysql.connector.Error as err:
            flash(f"Database error: {err}")
            return redirect(url_for('login'))
        finally:
            cursor.close()
            connection.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            print(f"User logged in: {session['user_id']}")  # Debugging statement
            return redirect(url_for('dashboard'))
        else:
            flash("Login Failed. Please check your name and your password!")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        print(f"User ID in session: {user_id}")  # Debugging statement
        
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM new_users WHERE id=%s", (user_id,))
            user = cursor.fetchone()
        finally:
            cursor.close()
            connection.close()
        
        if user:
            return render_template('dashboard.html', user=user)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Log out Successfully")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
