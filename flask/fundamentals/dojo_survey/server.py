from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'alright then, keep your secrets'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def submit_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def show_info():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)