from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("/play")

@app.route('/play')
def lvl_one():
    return render_template("index.html", box_color="#D8E2F2", times=3)
# NOTE: the variables "phrase" and "times" need to be written
# exactly the same way in the HTML so the value stored can be passed.

@app.route('/play/<int:x>')
def lvl_two(x):
    return render_template("index.html", box_color="#D8E2F2", times=x)

@app.route('/play/<int:x>/<color>')
def lvl_three(x,color):
    return render_template("index.html", box_color=color, times=x)

@app.route('/<path:undefined_route>')
def invalid_route(undefined_route):
    valid_routes = [
        "/play",
        "/play/<number_of_boxes>",
        "/play/<number_of_boxes>/<color>",
    ]
    message = "Please enter a valid route."
    return render_template("index.html", message=message, valid_routes=valid_routes)

if __name__=='__main__':
    app.run(debug=True, port=5001)