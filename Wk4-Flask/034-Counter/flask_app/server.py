from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

"""NOTES
if 'key_name' in session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")

session.clear()		# clears all keys
session.pop('key_name')		# clears a specific key
"""

@app.route('/')
def index():
    """
    1. Have the root route render a template that displays todo the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
    """
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    
    # * Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality
    visit_count = session.get("visit_count", 0)
    session["visit_count"] = visit_count+1
    return render_template('index.html', visits=visit_count)

@app.route('/increment_by_two')
def increment_by_two():
    """
    2. NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
    """
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return redirect('/')

@app.route('/increment_custom', methods=['POST'])
def increment_custom():
    """5. Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
    """
    increment_value = int(request.form.get('increment', 1))
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += (increment_value-1)
    return redirect('/')

@app.route('/destroy_session')
def reset():
    """
    3. Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
    4. Add a Reset button to reset the counter

    """
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, port=5001)