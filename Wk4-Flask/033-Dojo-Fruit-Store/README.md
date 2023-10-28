# Double-Charging Dojo Fruit Store

**Dojo Fruit Store** is a simple web application for ordering fruits for students. This README provides an overview of the project structure and how each route works.

### Table of Contents

1. [Project Structure](#project-structure)
2. [Templates](#templates)
3. [Server Logic](#server-logic)
4. [Data Flow](#data-flow)
5. [Running the Application](#running-the-application)

## Project Structure

The project consists of the following components:

- `templates` directory: Contains HTML templates for the application.
- `static` directory: Contains static files like CSS and images.
- `server.py`: The Python script implementing the server and logic.

## Templates

### 1. `index.html`

This template is the landing page for the application. It provides a brief introduction to the Dojo Fruit Store and allows users to place fruit orders.

### 2. `checkout.html`

This template displays the order summary and user information after a successful checkout. It includes details about the ordered fruits and the total count.

### 3. `fruits.html`

This template is a placeholder for displaying information about available fruits for users to order.

## Server Logic

The server logic is implemented in `server.py`. It handles the following routes and their functionality:

### 1. `/`

- Route: `@app.route('/')`
- Description: Renders the landing page (`index.html`) where users can place fruit orders.

### 2. `/checkout`

- Route: `@app.route('/checkout', methods=['POST'])`
- Description: Handles the submission of user orders. It performs the following tasks:
  - Validates user data, ensuring the provision of first name and last name.
  - Validates an optional student ID using a regular expression.
  - Validates that at least one fruit is selected for checkout.
  - Calculates the total fruit count.
  - Stores the user's order information in the session.
  - Renders the `checkout.html` template with order details.

### 3. `/fruits`

- Route: `@app.route('/fruits')`
- Description: Displays a placeholder page (`fruits.html`) that lists available fruits for ordering.


## Data Flow

Dojo Fruit Store keeps track of order information using the Flask `session` object. Here's how the data flows in the application:

1. **Order Submission (`/checkout` route):**

   - When a user submits their order on the `checkout.html` page, the form data is sent to the `/checkout` route via a POST request.

   - In the `/checkout` route, the server performs the following steps:

     - Validates user data, ensuring that the user provides their first name and last name.

     - Validates an optional student ID using a regular expression (`is_valid_student_id()` function).

     - Validates that at least one fruit is selected for checkout.

     - Calculates the total fruit count for the order.

     - The user's order information, including first name, last name, student ID (if provided), and the quantities of selected fruits, is stored in the Flask `session` object. This allows the server to keep track of the order information across multiple requests.

   - The server renders the `checkout.html` template, which displays the order summary and user information.

2. **Order Display (`checkout.html` template):**

   - The `checkout.html` template retrieves and displays the order information from the Flask `session` object.

   - Users can see a summary of their order, including fruit quantities and total count, along with their first name, last name, and optional student ID.

This data flow ensures that the order information is retained and displayed accurately during the user's session. The use of the `session` object in Flask allows for persistent storage of user-specific data throughout the user's interaction with the application.


## Running the Application

Activate the Virtual Environment pipenv shell And start the server: `python3 server.py` The app will run in debug mode on http://localhost:5001/. You can access the various routes to see how the content is dynamically rendered using Jinja2 templates.

**NOTES:**
- To see how this Flask application was initially set up, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/Lecture-Code/D9-Templates_Jinja_and_Static_Files/README.md#initial-setup).

---
<p align="right">Completed: ２０２３年１０月２８日（土）</p>