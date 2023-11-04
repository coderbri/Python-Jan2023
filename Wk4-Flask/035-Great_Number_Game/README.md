# Great Number Game

**Great Number Game** is a simple web application built with Flask that challenges users to guess a randomly generated number between 1 and 100. The user has a maximum of 5 attempts to guess the correct number. If they don't guess correctly within those 5 attempts, a "You Lose" message is displayed, and they can try again.

### Table of Contents

1. [**Routes and Their Functions**](#routes-and-their-functions)
    - [Root Route](#1-root-route)
    - [Submit Guess `POST` Route](#2-submit-guess-post)
    - [Reset Game](#3-reset-game)
    - [Game Over](#4-game-over)
2. [**Server Logic**](#server-logic)
    - [How is session used for this project?](#how-is-session-used-for-this-project)
3. [**Templates**](#templates)

## Routes and Their Functions

<!-- <div align="center">
<img src="./imgs" width="450px" height="auto">
</div> -->

#### 1. Root Route

- Route: `/`
- Description: Displays the main game page. Generates a random number for users to guess. Tracks the number of attempts and handles redirection to the success or game over pages.

#### 2. Submit Guess (`POST`)

- Route: `/submit_guess`
- Description: Handles user guesses, limiting them to a maximum of 5 attempts. Tracks the guess count, redirects for correct guesses, or provides feedback for incorrect ones.

#### 3. Reset Game

- Route: `/reset_game`
- Description: Allows users to reset the game by clearing session data, and redirects to the main game page for a new game.

#### 4. Game Over

- Route: `/game_over`
- Description: Displays a "You Lose" message for users exceeding the maximum attempts. Provides a "Try Again" button to start a new game.


## Server Logic

The **Great Number Game** is powered by Flask, a web framework. It utilizes session management for security and user interaction. The logic involves generating a random number for users to guess, tracking guess counts, and maintaining a seamless gaming experience.

### How is session used for this project?

- `guess_count` : Session stores user's guess count to limit attempts to 5.
- `num_to_guess` : Session stores the correct number for consistency and hidden display.


## Templates

- **`index.html`** : Displays the main game page, allows user input and feedback, and handles redirection.
- **`game_over.html`** : Displays the "You Lose" message for users exceeding maximum attempts. Provides a "Try Again" button for a new game.



**NOTES:**
- To see how this Flask application was initially set up, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/Lecture-Code/D9-Templates_Jinja_and_Static_Files/README.md#initial-setup).
- For more information on screen-height adjustment, [check this project](https://github.com/coderbri/Python-Jan2023/blob/main/Wk4-Flask/030-Playground/README.md#screen-height-adjustment).

---
<p align="right">Completed: ２０２３年１１月０３日（金）</p>

