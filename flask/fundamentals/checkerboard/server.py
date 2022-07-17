from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board():
    return render_template('index.html', row=8, col=8, color1='black', color2='red')

@app.route('/<int:x>')
def board_rows(x):
    return render_template('index.html', row=x, col=8, color1='black', color2='red')

@app.route('/<int:x>/<int:y>')
def rows_and_cols(x,y):
    return render_template('index.html', row=x, col=y, color1='black', color2='red')

@app.route('/<int:x>/<int:y>/<string:one>')
def rows_and_cols_color1(x,y,one):
    return render_template('index.html', row=x, col=y, color1=one, color2='red')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def rows_and_cols_color2(x,y,one,two):
    return render_template('index.html', row=x, col=y, color1=one, color2=two)

if __name__ =="__main__":
    app.run(debug=True)