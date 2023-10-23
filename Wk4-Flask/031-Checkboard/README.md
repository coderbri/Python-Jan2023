# Checkerboard

This Flask application allows you to generate custom checkerboards with different sizes and color combinations. It provides multiple routes to customize your checkerboard according to your preferences.

### Table of Contents

1. [Routes and Their Functions](#routes-and-their-functions)
2. [Summary](#summary)
2. [Running the Appication](#running-the-application)


## Routes and Their Functions

#### 1. Default 8x8 Checkerboard

- Route: `/`
- Description: Renders an 8x8 standard checkerboard with default colors.
- Example URL: `http://localhost:5001/`

#### 2. Custom Rows and Columns

<div align="center">
<img src="./imgs/Route-2-Demo.gif" width="450px" height="auto">
</div>

- Route: `/<int:x>/<int:y>`
- Description: Renders a custom-sized checkerboard with the specified number of rows and columns using default colors.
- Example URL: `http://localhost:5001/6/10` (To create a 6x10 checkerboard)

#### 3. Custom Size and Colors

<div align="center">
<img src="./imgs/Route-3-Demo.gif" width="450px" height="auto">
</div>
<div align="center">
<img src="./imgs/Route-4-Demo.gif" width="450px" height="auto">
</div>

- Route: `/<int:x>/<int:y>/<color1>/<color2>`
- Description: Renders a custom-sized checkerboard with the specified number of rows and columns using custom colors.
- Example URL: `http://localhost:5001/5/5/blue/yellow` (To create a 5x5 checkerboard with blue and yellow colors)


### Summary

1. Navigate to the main route to view an 8x8 standard checkerboard with default colors.
    - The `checkerboard()` route renders an 8x8 standard checkerboard with default colors.
    - The `render_4_by_8()` route renders a 4x8 standard checkerboard with default colors.

2. Use custom routes to specify the number of rows, columns, and colors according to your preferences.
    - The `render_by_x_and_y(x, y)` route allows you to specify the number of rows and columns for your custom checkerboard using default colors.
    - The `render_custom(x, y, color1, color2)` route enables you to create a custom-sized checkerboard with specific colors.

3. If you enter an invalid route, you'll receive a message with instructions on the valid URL formats.
    - The application also provides a list of example URL formats for each route.
<div align="center">
<img src="./imgs/Route-Undefined-Demo.gif" width="450px" height="auto">
</div>


### Running the Application

Activate the Virtual Environment pipenv shell And start the server: python3 server.py The app will run in debug mode on http://localhost:5001/. You can access the various routes to see how the content is dynamically rendered using Jinja2 templates.

**NOTES:**
- To see how this Flask application was initially set up, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/Lecture-Code/D9-Templates_Jinja_and_Static_Files/README.md#initial-setup).
- For more information on screen-height adjustment, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/030-Playground/README.md#screen-height-adjustment).


---
<p align="right">Completed: ２０２３年１０月１５日（日）</p>