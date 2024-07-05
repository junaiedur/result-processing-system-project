from flask import Flask, render_template
# from flask import request, Blueprint, abort, session, redirect, url_for
# from jinja2 import TemplateNotFound

app = Flask(__name__)
app.secret_key = b'__u53r!53Y13rc35'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result/")
def result():
    return render_template("result.html")

@app.route("/about/")
def about():
    return render_template("about-us.html")
@app.route("/contact/")
def contact():
    return render_template("contact-us.html")

@app.route("/privacy-policy/")
def privacyPolicy():
    return render_template("privacy-policy.html")

@app.route("/licencing/")
def licencing():
    return render_template("licence.html")

if __name__ == "__main__":
    app.run(debug=True)
