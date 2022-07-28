from flask import Flask, render_template, redirect, session, request
import random
app = Flask (__name__)
app.secret_key = "im in love with the secrets"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['winnings'] = []
    print(session['gold'], "in the bank")
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    if request.form['get_gold'] == 'rice_paddy':
        temp = random.randint(10,20)
        session['gold'] += temp
        print(f"Earned {temp} gold from the rice paddy!")
    if request.form['get_gold'] == 'hideout':
        temp = random.randint(5,10)
        session['gold'] += temp
        print(f"Found {temp} gold in the hideout!")
    if request.form['get_gold'] == 'yashiki':
        temp = random.randint(2,5)
        session['gold'] += temp
        print(f"Borrowed {temp} gold from the yashiki!")
    if request.form['get_gold'] == 'dice_den':
        temp = random.randint(-50,50)
        session['gold'] += temp
        print(f"Gambling at the dice den resulted in {temp} gold")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)