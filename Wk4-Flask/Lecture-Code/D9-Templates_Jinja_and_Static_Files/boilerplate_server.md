This is a generally how the server.py will look for these simple flask projects (not modularized):

```python
from flask import Flask, render_template
app = Flask(__name__)



if __name__=='__main__':
    app.run(debug=True, port=5001)
    ```