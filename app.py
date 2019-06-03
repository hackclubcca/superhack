from flask import Flask, render_template
from flask_wtf import Form
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


"""


Add a contact form


"""

if __name__ == '__main__':
    app.run(debug=True)
