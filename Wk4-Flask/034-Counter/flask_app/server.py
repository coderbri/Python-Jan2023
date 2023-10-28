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
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    
    visit_count = session.get("visit_count", 0)
    session["visit_count"] = visit_count+1
    return render_template('index.html', visits=visit_count)

@app.route('/increment_by_two')
def increment_by_two():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return redirect('/')

@app.route('/increment_custom', methods=['POST'])
def increment_custom():
    increment_value = int(request.form.get('increment', 1))
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += (increment_value-1)
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)