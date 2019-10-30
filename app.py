from flask import Flask, render_template, make_response, request
from flask_sitemap import Sitemap
from flask_assets import Environment, Bundle

app = Flask(__name__, static_folder='static', static_url_path='')
smp = Sitemap(app=app)
assets = Environment(app)
scss = Bundle('scss/index.scss',
              filters='scss', output='gen/all.css')
assets.register('scss', scss)

STATIC_URL = "/static/"


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
