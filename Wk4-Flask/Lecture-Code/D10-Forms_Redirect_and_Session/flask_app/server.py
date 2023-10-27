from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    
    return render_template('index.html')

# @app.route('/user/create')
# def create_user():
#     return "User has been created!"
"""
? Submiting the form will run the route above as a GET request,
? generating a URL as the following:
* http://localhost:5001/?first_name=Jane&last_name=Doe&email=jdoe%40gmail.com
! This is bad practice and the route should handle the data inputed as a POST method
"""

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    """
    print(request.form) will log the following output:
    ImmutableMultiDict([('first_name', 'Jane'), ('last_name', 'Doe'), ('email', 'jdoe@test.com')])
    This contains the key:val pairs from the form tag in the html (i.e., label:input) and is packaged up to an immutable dict in request.form.
    So we'll access the values via key names: request.form['first_name'] = Jane
    """
    # return "User has been created!"
    print("*** User has been created! ***")
    
    # * Now we need to tranfer the request.form data to the "show" route.
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    # session['user'] = request.form # ? {'email': 'jdoe@test.com', 'first_name': 'Jane', 'last_name': 'Doe'}
    return redirect('/user/show')

@app.route('/user/show')
def show_user():
    # * Retrieve the information from session.
    return render_template('show_user.html', user=request.form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)