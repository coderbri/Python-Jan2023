from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    
    if not name or not location or not language:
        error_message = "Please fill out all required fields."
        return render_template('index.html', error_message=error_message)
    
    form_data = {
        'name': name,
        'location': location,
        'language': language,
        'comments': request.form['comments']
    }
    session['form_data'] = form_data
    
    return redirect('/results')

@app.route('/results')
def results():
    form_data = session.get('form_data', {})
    return render_template('results.html', user_result=form_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)