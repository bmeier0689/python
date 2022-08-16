from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def one_dojo(id):
    data = {
        'id': id
    }
    return render_template("one_dojo.html", dojo = Dojo.get_dojo_with_ninjas(data))