from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return "안녕~"

"""
@app.route('/say/<name>')
def say_name(name):
    return f"<h1>안녕하세요. 제 이름은 {name}입니다.</h1>
? Just like we can pass path variable as above, we can pass them into our rendered template using Jinja2.
"""

@app.route('/say/<name>')
def say_name(name):
    return render_template('index.html', name_to_display=name)
    # ? jinja_variable_to_pass_to_template = variable_passed_from_here_in_server_url

@app.route('/say/<name>/<int:times>')
def repeat(name, times):
    return render_template('repeat_name.html', name_to_display=name, repeated_times=times)

@app.route('/display_list')
def loop_through_list():
    student_list = [
        {'name': 'Micahel', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template('student_list.html', student_info=student_list)

if __name__=='__main__':
    app.run(debug=True, port=5001)