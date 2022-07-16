from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', num=3, color="skyblue")

@app.route('/play/<int:num>')
def add_boxes(num):
    return render_template('index.html', num=7, color="skyblue")

@app.route('/play/<int:num>/<string:color>')
def add_more_boxes(num, color):
    return render_template('index.html', num=num, color=color)

if __name__ =="__main__":
    app.run(debug=True)