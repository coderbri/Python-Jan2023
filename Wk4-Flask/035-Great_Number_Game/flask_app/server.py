from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def index():
    # ? Setup the random integer in the game, hidden from user for them to guess - random will generate this int
    if "num_to_guess" not in session:
        session["num_to_guess"] = random.randint(1,100)
    
    # ? Track user's guesses
    guess_count = session.get("guess_count", 0)
    session["guess_count"] = guess_count+1
    
    return render_template('index.html', guesses=guess_count)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    # ? Validating Input
    user_guess = request.form['guess'].strip()
    if not user_guess:
        error_message = "Please enter a valid guess."
        return render_template('index.html', error=error_message)
    
    # ? Limit to only 5 attempts
    if session['guess_count'] >= 5:
        return redirect('/game_over')
    
    # ? save the user's guess num (input from the form) in session for the webapp to check with the random int in session
    session['guess'] = int(request.form['guess']) # ? int() will typecast the str into an int
    
    return redirect('/')

@app.route('/reset_game')
def reset():
    session.clear()
    return redirect('/')

@app.route('/game_over')
def game_over():
    session.clear()
    return render_template('game_over.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)