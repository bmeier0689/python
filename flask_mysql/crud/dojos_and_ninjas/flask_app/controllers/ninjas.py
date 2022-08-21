from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/new_ninja')
def new_ninja():
    return render_template("new_ninja.html", dojos = Dojo.get_all())

@app.route('/add_ninja', methods=["POST"])
def add_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')

@app.route('/edit_ninja/<int:ninja_id>')
def edit_ninja(ninja_id):
    data = {
        'ninja_id': ninja_id
    }
    ninja = Ninja.get_one_ninja(data)[0]
    return render_template('/edit_ninja.html', ninja = ninja)

@app.route('/update_ninja', methods=["POST"])
def update_ninja():
    print(request.form)
    Ninja.update_ninja(request.form)
    return redirect(f'/dojo/{request.form["dojo_id"]}')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Ninja.delete_ninja(data)
    return redirect(request.referrer)