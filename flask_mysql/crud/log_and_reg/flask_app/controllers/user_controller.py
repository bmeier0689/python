from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'dob': request.form['dob'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    if User.validate_user(request.form):
        session['user_id'] = User.save(data)
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    user = User.check_email(request.form['email'])
    if user == False:
        flash("Login credentials incorrect")
        return redirect('/')
    else:
        if bcrypt.check_password_hash(user.password, request.form['password']) == True:
            session['user_id'] = user.id
            return redirect('/login_success')
        else:
            flash("Incorrect password")
            return redirect('/')

@app.route('/login_success')
def login_success():
    return render_template('login_success.html')