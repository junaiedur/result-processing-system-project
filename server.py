from flask import Flask, Blueprint, render_template, abort, session, redirect, url_for, request
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.secret_key = b'__u53r!53Y13rc35'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
