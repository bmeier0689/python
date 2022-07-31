from flask import Flask, render_template, redirect, session, request
import random
app = Flask (__name__)
app.secret_key = "im in love with the secrets"

@app.route('/')
def index():
    if 'gold' not in session:
        session['tries'] = 15
        session['gold'] = 0
        session['earnings'] = []
        session['losses'] = []
    if session['tries'] == 0:
        session['gold'] = 0
        session['earnings'] = []
        session['losses'] = []
        session['tries'] = 15
        print('All session parameters reset to defaults')
    print(session['gold'], "in the bank")
    print(session['tries'], "tries remaining")
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    if request.form['get_gold'] == 'rice_paddy':
        temp = random.randint(10,20)
        session['gold'] += temp
        earning = session['earnings']
        earning.append(f"Your hard work paid off, you earned {temp} gold from the rice paddy!")
        session['earnings'] = earning
        tries = session['tries']
        session['tries'] -= 1
        print(f"Your hard work paid off, you earned {temp} gold from the rice paddy!")
    if request.form['get_gold'] == 'hideout':
        temp = random.randint(5,10)
        session['gold'] += temp
        earning = session['earnings']
        earning.append(f"After rummaging around in the cushions, you found {temp} gold in the hideout!")
        session['earnings'] = earning
        tries = session['tries']
        session['tries'] -= 1
        print(f"After rummaging around in the cushions, you found {temp} gold in the hideout!")
    if request.form['get_gold'] == 'castle':
        temp = random.randint(2,5)
        session['gold'] += temp
        earning = session['earnings']
        earning.append(f"While no one was looking, you stole {temp} gold from the castle!")
        session['earnings'] = earning
        tries = session['tries']
        session['tries'] -= 1
        print(f"While no one was looking, you stole {temp} gold from the castle!")
    if request.form['get_gold'] == 'dice_den':
        temp = random.randint(-50,50)
        if temp >= 0:
            session['gold'] += temp
            earning = session['earnings']
            earning.append(f"Nice! You gained {temp} gold while gambling at the dice den!")
            session['earnings'] = earning
            tries = session['tries']
            session['tries'] -= 1
            print(f"Nice! You gained {temp} gold while gambling at the dice den!")
        elif temp <= 0:
            session['gold'] += temp
            losses = session['losses']
            losses.append(f"Aww, too bad! Your wallet is now {temp} gold lighter!")
            session['losses'] = losses
            tries = session['tries']
            session['tries'] -= 1
            print(f"Aww, too bad! Your wallet is now {temp} gold lighter!")
    if request.form['get_gold'] == 'reset_game':
        session['gold'] = 0
        session['earnings'] = []
        session['losses'] = []
        session['tries'] = 15
        print('All session parameters reset to defaults')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)