from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return num * name

@app.errorhandler(404)
def not_found_error(error):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)
