from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypy = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypy.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.save(data)
    return redirect('/recipes')

@app.route('/login', methods=['POST'])
def login():
    user = User.check_email(request.form['email'])
    if user == False:
        flash("Please enter a valid email address", "login")
        return redirect('/')
    else:
        if bcrypy.check_password_hash(user.password, request.form['password']) == True:
            session['user_id'] = user.id
            return redirect('/recipes')

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    recipes = Recipe.get_all()
    print(recipes)
    return render_template("recipes.html", all_recipes = recipes)

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    print(request.form)
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    print(request.form)
    Recipe.update_recipe(request.form)
    return redirect('/recipes')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Recipe.delete_recipe(data)
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')