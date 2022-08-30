from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.cookie_order import Cookie_order

@app.route('/')
def index():
    return redirect('/orders')

@app.route('/orders')
def orders():
    orders = Cookie_order.get_all()
    print(orders)
    return render_template('index.html', all_orders = orders)

@app.route('/edit_order/<int:id>')
def edit_order(id):
    data = {
        'id': id
    }
    order = Cookie_order.get_one_order(data)[0]
    return render_template('/edit_order.html', order = order)

@app.route('/update_order', methods=["POST"])
def update_order():
    print(request.form)
    if Cookie_order.validate_order(request.form):
        Cookie_order.update_order(request.form)
        return redirect('/')
    return redirect(request.referrer)

@app.route('/add_order')
def add_order():
    return render_template('add_order.html')

@app.route('/new_order', methods=["POST"])
def new_order():
    print(request.form)
    if Cookie_order.validate_order(request.form):
        Cookie_order.save(request.form)
        return redirect('/')
    return redirect(request.referrer)
