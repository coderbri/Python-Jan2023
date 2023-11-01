from flask import Flask, render_template
# from flask library, import Flask class
app = Flask(__name__)

# * The Root Route
# ? Establish this first to avoid encountering 404 error, or "route not found"
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/kr')
def say_hello_in_korean():
    return '안녕하세요~!'

# * Path Variable
#            /number/7
@app.route('/number/<num>')
def test_path_var( num ):
    return num # the number '7' will be returned on this URL

@app.route('/hello/<name>')
def hello_user( name ):
    return f"Hello, {name}!"

# * Type Converters
@app.route('/hello/<name>/<int:num>')
def repeat_hello( name, num ):
    return f"<h2>Hello, {name * num}!</h2>"


# * Render Templates
@app.route('/home_page')
def render_html():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True, port=5001)
# ? For Mac users, specify port=5001 as port=5000 is occupied for Apple AirPlay