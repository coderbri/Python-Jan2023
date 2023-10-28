from flask import Flask, render_template, request, redirect, session, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    return render_template('index.html')


# ? Validation Function: Student ID
def is_valid_student_id(student_id):
    import re
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, student_id) is not None

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    form_data = request.form
    # ? Current Date
    current_datetime = datetime.now()
    
    # ? User Validation Check
    first_name = form_data.get('first_name')
    last_name = form_data.get('last_name')
    if not first_name or not last_name:
        flash('Please provide your first name and last name.')
        return redirect(url_for('index'))
    
    student_id = form_data.get('student_id')
    if student_id and not is_valid_student_id(student_id):
        flash('Please provide a valid student ID (e.g., 123-456-7890).')
        return redirect(url_for('index'))
    
    # ? Fruit Quantity Logic
    total_fruit_count = 0
    valid_fruits = ['strawberry', 'raspberry', 'apple', 'blackberry']
    for fruit, quantity in form_data.items():
        if fruit in valid_fruits:
            try: # int("1")+int("2")+int("3") # returns 6 
                quantity = int(quantity) 
                total_fruit_count += quantity
            except ValueError:
                pass
    if total_fruit_count == 0:
        flash('Please select at least one fruit for checkout.')
        return redirect(url_for('index'))
    
    # * Data Passing to HTML
    session['checkout_info'] = form_data
    session['total_fruit_count'] = total_fruit_count
    print(f"Checking {form_data['first_name']} for {total_fruit_count} fruits.")
    return render_template("checkout.html", today=current_datetime)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True, port=5001)