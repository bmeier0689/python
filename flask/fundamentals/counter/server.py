from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'secrets dont make friends'

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/increment')
def increment():
    session["count"] += 1
    return redirect('/')

@app.route('/userInc', methods=["POST"])
def userInc():
    session["count"] += int(request.form['num'])
    session["count"] -= 1
    print(session["count"])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)