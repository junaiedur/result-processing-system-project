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
    return "About Us!"

@app.route("/contact/")
def contact():
    return "Contact Us!"

@app.route("/privacy-policy/")
def privacyPolicy():
    return "Our Privacy Policy!"

@app.route("/licencing/")
def licencing():
    return "Our Licencing Policy!"

if __name__ == "__main__":
    app.run(debug=True)
