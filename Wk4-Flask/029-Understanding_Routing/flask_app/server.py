from flask import Flask, render_template
app = Flask(__name__)

# localhost:5001/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

# localhost:5001/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# localhost:5001/say/flask - have it say "Hi Flask!"
@app.route('/say/flask')
def sayFlask():
    return "Hi Flask!"

# localhost:5001/say/michael - have it say "Hi Michael!"
# localhost:5001/say/john - have it say "Hi John!"
@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name}!"

# localhost:5001/repeat/35/hello - have it say "hello" 35 times
# localhost:5001/repeat/80/bye - have it say "bye" 80 times
# localhost:5001/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:repeated_num>/<phrase>')
def repeat_phrase( repeated_num, phrase ):
    return f"{ repeated_num * phrase }"


if __name__=='__main__':
    app.run(debug=True, port=5001)