import flask
import os

os.chdir("./mysite/")
app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/sig")
def sig():
    return "sig sim"