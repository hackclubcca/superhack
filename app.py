from flask import Flask, render_template, make_response, request
from flask_sitemap import Sitemap
from datetime import datetime, timedelta
from flask_assets import Environment, Bundle

app = Flask(__name__, static_folder='static', static_url_path='')
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


@app.route('/document/prospectus.pdf')
def document(name):
    return render_template("document.html", document_name="prospectus.pdf")


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    pages = []
    ten_days_ago = datetime.now() - timedelta(days=3)
    for rule in app.url_map.iter_rules():
        if 'GET' in rule.methods and len(rule.arguments) == 0 and not rule.rule.startswith('/admin'):
            pages.append(['https://superhack.org' + rule.rule, ten_days_ago])
    sitemap_template = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_template)
    response.headers["Content-Type"] = "application/xml"
    return response


if __name__ == '__main__':
    app.run(debug=True)
