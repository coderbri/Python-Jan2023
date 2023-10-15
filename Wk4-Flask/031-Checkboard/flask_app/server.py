from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    # return 'Hello World!'
    return render_template('index.html', row=8, col=8, color_primary='red', color_secondary='black')

@app.route('/4')
def render_4_by_8():
    return render_template('index.html', row=4, col=8, color_primary='red', color_secondary='black')

@app.route('/<int:x>/<int:y>')
def render_by_x_and_y(x,y):
    return render_template('index.html', row=x, col=y, color_primary='red', color_secondary='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def render_custom(x,y,color1,color2):
    return render_template('index.html', row=x, col=y, color_primary=color1, color_secondary=color2)

@app.route('/<path:undefined_route>')
def invalid_route(undefined_route):
    message = "Please enter a valid route."
    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)