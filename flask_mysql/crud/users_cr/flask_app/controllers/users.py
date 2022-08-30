from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/new_user')
def new_user():
    return render_template('add_user.html')

@app.route('/add_user', methods=["POST"])
def add_user():
    print(request.form)
    if User.validate_user(request.form):
        User.save(request.form)
        return redirect('/')
    return redirect(request.referrer)

@app.route('/user/<int:id>')
def one_user(id):
    data = {
        'id': id
    }
    user = User.get_one_user(data)[0]
    return render_template("one_user.html", user = user)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    user = User.get_one_user(data)[0]
    return render_template('/edit_user.html', user = user)

@app.route('/update', methods=["POST"])
def update_user():
    print(request.form)
    User.update_user(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/')