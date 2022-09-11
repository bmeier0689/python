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
    if bcrypy.check_password_hash(user.password, request.form['password']) == False:
        flash("Please input a valid password", "login")
        return redirect('/')
    else:
        if bcrypy.check_password_hash(user.password, request.form['password']) == True:
            session['user_id'] = user.id
            return redirect('/recipes')

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    recipes = Recipe.get_all()
    return render_template('recipes.html', all_recipes = recipes, user = User.get_by_id(data))

@app.route('/one_recipe/<int:id>')
def one_recipe(id):
    data = {
        'id': id
    }
    user_name = {
        'id': session['user_id']
    }
    recipe = Recipe.get_one_recipe(data)[0]
    return render_template('recipe.html', recipe = recipe, user = User.get_by_id(user_name))

@app.route('/new_recipe')
def new_recipe():
    if 'user_id' in session:
        return render_template('new_recipe.html')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/new_recipe')
    print(request.form)
    user_id = session['user_id']
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_one_recipe(data)[0]
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect(request.referrer)
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