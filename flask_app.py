import flask
import os
import json

def getJSON(path):
    with open(path) as f:
        return json.load(f)
    
def writeJSON(path, content):
    with open(path, "w") as f:
        json.dump(content, f, skipkeys=True, indent=4)

def logged_in():
    return "logged_in" in flask.session and flask.session["logged_in"] == True and "user" in flask.session

# os.chdir("./mysite/")
app = flask.Flask(__name__)
app.secret_key = "123"

@app.route("/", methods=["GET", "POST"])
def index():
    warning = ""
    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        psw = flask.request.form.get("psw")
        if name is not None and name in getJSON("data/users.json"):
            flask.session.clear()
            flask.session["logged_in"] = True
            flask.session["user"] = name
        else:
            warning = f"Name '{name}' not in list"
    return flask.render_template("index.html", warning=warning)

@app.route("/logout")
def logout():
    flask.session.clear()
    return flask.redirect(flask.url_for("index"))

@app.route("/sig")
def sig():
    if not logged_in(): return flask.redirect(flask.url_for("index"))
    return "sig sim"

app.run()