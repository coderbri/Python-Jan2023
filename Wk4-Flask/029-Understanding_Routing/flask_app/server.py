from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/flask')
def sayFlask():
    return "Hi Flask!"

@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:repeated_num>/<phrase>')
def repeat_phrase( repeated_num, phrase ):
    return f"{ repeated_num * phrase }"

@app.route('/<path:undefined_route>')
def handle_undefined_route(undefined_route):
    return "Sorry! No response. Try again."

if __name__=='__main__':
    app.run(debug=True, port=5001)