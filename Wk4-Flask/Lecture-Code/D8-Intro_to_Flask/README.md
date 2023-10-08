### ２０２３年１０月０７日（土）

---

## Topics to Cover

- **Intro to Flask**
    - Overview
    - Virtual Environments
    - Hello Flask
    - Routes
    - Rendering Views

### Buidling the Application

1. Inside the **project_folder**, create a file called **server.py**.
    - this is where all of our routes will be set up to handle the requests.
    - The following code is added into the **server.py**:
    ```py
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    
    if __name__=='__main__':
        app.run(debug=True)
    ```

2. Now run the following command:
    ```
    pipenv install flask
    ```
    If the above doesn't work, try this:
    ```
    python3 -m pipenv install flask
    ```
    Two files will apper (Pipfile and Pipfile.lock). They're both needed to use the installed packages. Pipfile has the packages installed whereas Pipfile.lock has the specific details on what version is being used.

3. Activate the Virtual Environment
    ```
    pipenv shell
    ```