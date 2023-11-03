from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True, port=5001)