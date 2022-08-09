from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

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
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/edit_user')
def edit_user():
    User.edit_user
    return render_template('edit_user.html')

@app.route('/show_user')
def show_user():
    user = User.show_user()
    print(user)
    return render_template('show_user.html', user = user)

@app.route('/delete_user')
def delete_user():
    User.delete_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)