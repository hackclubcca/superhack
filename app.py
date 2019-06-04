from flask import Flask, render_template
from wtforms import Form
from flask_assets import Environment, Bundle
app = Flask(__name__)
assets = Environment(app)
scss = Bundle('scss/index.scss',
            filters='scss', output='gen/all.css')
assets.register('scss', scss)


@app.route('/')
def index():
    return render_template("index.html")


"""


Add a contact form


"""

if __name__ == '__main__':
    app.run(debug=True)
