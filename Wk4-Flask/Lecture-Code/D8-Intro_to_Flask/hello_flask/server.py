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

# * Render Templates
@app.route('/home_page')
def render_html():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)