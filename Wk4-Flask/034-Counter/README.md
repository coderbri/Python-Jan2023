# Counter

This is a simple Flask web application that demonstrates how to use sessions to build a counter. The app provides the following functionality:

### Table of Contents

1. [Routes and Their Functions](#routes-and-their-functions)
2. [Summary](#summary)
2. [Running the Appication](#running-the-application)


## Routes and Their Functions

#### 1. Root Route

<div align="center">
<img src="./imgs/counter-full_demo.gif" width="450px" height="auto">
</div>

- Route: `/`
- Description: Renders the number of times the client has visited the site and the current value of the counter. The counter is incremented each time the user visits the page. Refreshing the page will also increment the counter.
- Example URL: `http://localhost:5001/`

#### 2. Increment by Two

<div align="center">
<img src="./imgs/counter-increment_by_2-demo.gif" width="450px" height="auto">
</div>

- Route: `/increment_by_two`
- Description: Clicking the "Add 2" button will increase the counter by 2. After incrementing, it redirects back to the home route.

#### 3. Custom Increment

<div align="center">
<img src="./imgs/counter-increment_custom-demo.gif" width="450px" height="auto">
</div>

- Route: `/increment_custom`
- Description: Renders a form that allows the user to specify the increment value for the counter. Users can input their desired increment value and click the "Increment" button. The counter will be incremented by the specified value.
   - The counter can be incremented by any positive integer value.
   - After incrementing, it redirects back to the home route.

#### 4. Reset Session Route

- Route: `/destroy_session`
- Description: Clicking the "Reset" button clears the session, resetting both the visit count and the counter to zero. After resetting, it redirects back to the home route.


### Session Concept

The app uses Flask's built-in session management to store and maintain user data. Session variables are temporary and associated with a specific user's session. In this app, two key session variables are used:

- **`visit_count`**: This variable keeps track of the number of times the user has visited the page. It is incremented each time the user accesses the home route.

- **`count`**: This variable stores the current value of the counter. It is incremented based on user actions, including the "+2" button and the custom increment form.

By using sessions, the app can store and update these variables for each user's session, providing a personalized and dynamic user experience.

### Running the Application

Activate the Virtual Environment pipenv shell And start the server: python3 server.py The app will run in debug mode on http://localhost:5001/. You can access the various routes to see how the content is dynamically rendered using Jinja2 templates.

**NOTES:**
- To see how this Flask application was initially set up, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/Lecture-Code/D9-Templates_Jinja_and_Static_Files/README.md#initial-setup).
- For more information on screen-height adjustment, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/030-Playground/README.md#screen-height-adjustment).

---
<p align="right">Completed: ２０２３年１０月２７日（金）</p>