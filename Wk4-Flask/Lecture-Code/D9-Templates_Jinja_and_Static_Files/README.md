### ２０２３年１０月１２日（木）

---

## Topics to Cover

- **More Template Rendering with Jinja and Static Files**
    - More Template Rendering
    - Template Engines
    - Static Files

### Table of Contents
1. [Initial Setup](#initial-setup)
2. [Flask Web Application - Rendering with Jinja2](#flask-web-application---rendering-with-jinja2)
3. [Application Structure](#application-structure)
4. [Routes and Functions](#routes-and-functions)
5. [Jinja2 Templates](#jinja2-templates)
6. [Running the Application](#running-the-application)

---
### Initial Setup

<details>
<summary>Building the Application</summary>

1. Inside the **project_folder**, create a file called **server.py**.
    - This is where all of our routes will be set up to handle the requests.

    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True, port=5001)
    ```

2. Now run the following command:
    ```
    pipenv install flask
    ```
    If the above doesn't work, try this:
    ```
    python3 -m pipenv install flask
    ```
    Two files will appear (Pipfile and Pipfile.lock). They're both needed to use the installed packages. Pipfile has the packages installed, whereas Pipfile.lock has the specific details on what version is being used.
</details>


## Flask Web Application - Rendering with Jinja2

This Flask web application demonstrates how to use Jinja2 templates to render dynamic content. The app defines several routes, each showcasing different features and uses of Jinja2 for rendering HTML templates.

## Application Structure

The application consists of three main files:

1. `server.py`: The main Flask application file. It defines the routes and handles requests from users.

2. `index.html`, `repeat_name.html`, and `student_list.html`: Jinja2 HTML templates that are used for rendering dynamic content. These templates contain placeholders for variables that are filled with data from the server.

## Routes and Functions

1. **`/` Route (Root Route)**

    - URL: `/`
    - Function: `root()`
    - Description: The root route simply returns a Korean greeting, "안녕~." It doesn't use any HTML templates.

2. **`/say/<name>` Route**

    - URL: `/say/<name>`
    - Function: `say_name(name)`
    - Description: This route takes a parameter `name` and renders the `index.html` template. The template displays a greeting message using the provided `name`. It showcases how to pass variables to templates.

3. **`/say/<name>/<int:times>` Route**

    - URL: `/say/<name>/<int:times>`
    - Function: `repeat(name, times)`
    - Description: This route takes two parameters, `name` and `times`, and renders the `repeat_name.html` template. The template displays the provided `name` and repeats it a specified number of times. It also demonstrates the use of for loops in Jinja2 templates.

4. **`/display_list` Route**

    - URL: `/display_list`
    - Function: `loop_through_list()`
    - Description: This route renders the `student_list.html` template and passes a list of student information to it. The template uses a for loop to display the list of students and their ages.

## Jinja2 Templates

The application uses Jinja2 templates to render HTML with dynamic content. Here's a brief overview of the templates:

1. `index.html`: This template displays a personalized greeting message using the provided `name`.

2. `repeat_name.html`: This template extends the functionality of `index.html` by also displaying the number of times the name should be repeated. It provides examples of how to use variables and for loops in Jinja2 templates.

3. `student_list.html`: This template demonstrates how to loop through a list of student information and display it on the webpage.

## Running the Application

Activate the Virtual Environment
    ```
    pipenv shell
    ```
    And start the server:
    ```
    python3 server.py
    ```
The app will run in debug mode on http://localhost:5001/. You can access the various routes to see how the content is dynamically rendered using Jinja2 templates.
