from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    print(request.form)
    name = request.form.get('name')
    location = request.form.get('location')
    fav_language = request.form.get('fav_language')
    experience = request.form.get('experience') # ? .get() is used to display the selected radio from the options
    spoken_languages = request.form.getlist('spoken_languages') # ? .getlist() is used to display the selected checkbox(es) from the options
    
    if not name or not location or not fav_language or experience is None or not spoken_languages:
        error_message = "Please fill out all required fields."
        return render_template('index.html', error_message=error_message)
    
    form_data = {
        'name': name,
        'location': location,
        'fav_language': fav_language,
        'experience': experience,
        'spoken_languages': spoken_languages,
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