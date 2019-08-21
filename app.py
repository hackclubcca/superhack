from flask import Flask, render_template, make_response, request
from wtforms import Form
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)
scss = Bundle('scss/index.scss',
              filters='scss', output='gen/all.css')
assets.register('scss', scss)


@app.route('/')
def index():
    if not request.headers.get("USER_AGENT"):
        return "You found an easter egg! Email harris@ravenhack.org with the message 'I like turtles'"
    return render_template("index.html")


@app.route('/document/<name>')
def document(name):
    return render_template("document.html", document_name=name)


"""


Add a contact form


"""

if __name__ == '__main__':
    app.run(debug=True)
