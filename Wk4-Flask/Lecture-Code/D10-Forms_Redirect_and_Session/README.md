### ２０２３年１０月２７日（金）

---

## Topics to Cover

- **Forms, Redirect & Session**
    - POST Form Submission
        - POST vs GET
        - `request.form`
    - Redirecting
    - Session

### Table of Contents
1. [Overview](#overview)
2. [Routes and Descriptions](#routes-and-descriptions)
3. [Concepts Explained](#concepts-explained)
4. [Form Handling](#form-handling)
5. [Redirect](#redirect)
6. [Session Management](#session-management)
6. [Secret Key](#secret-key)


---

This is a simple Flask web application that demonstrates how to handle forms, use the `redirect` function, and manage user session data.

### Overview

This Flask app consists of three main components:

1. **Form Handling**: The app allows users to submit a form with their first name, last name, and email. The form data is processed in the `create_user` route, which handles the form submission.

2. **Redirect**: After processing the form data, the app uses the `redirect` function to redirect users to the `show_user` route, where the user's data is displayed.

3. **Session Management**: The user's data is stored in the Flask `session` object, allowing it to be accessed across different routes. This data persistence is used to display user information on the `show_user` page.

4. **Secret Key**: The Flask app uses a secret key, set using `app.secret_key`, to secure session data and protect against security vulnerabilities such as cross-site request forgery (CSRF) attacks.

## Routes and Descriptions

- `/`: The homepage where the form is displayed. Users can enter their information and submit the form.

- `/user/create` (POST): Handles the form submission, retrieves the form data using `request.form`, and stores it in the user's session. It then redirects to `/user/show`.

- `/user/show`: Displays the user's data stored in the session, allowing users to view their information.

## Concepts Explained

### Form Handling

The form data is sent as a POST request to the `/user/create` route. In this route, the form data is accessed using `request.form`, and the user's data is stored in the Flask `session` object.

### Redirect

After processing the form data, the app uses the `redirect` function to take users to the `/user/show` route, which displays the user's information. This allows for a cleaner URL and a better user experience.

### Session Management

The user's data is stored in the Flask `session` object. This session data can be accessed and used across different routes. In this app, it is used to display the user's first name, last name, and email on the `show_user` page.

### Secret Key

The `app.secret_key` is a crucial security measure in Flask. It is used to cryptographically secure the session data and protect against security vulnerabilities such as CSRF attacks. Always keep your secret key private and secure.