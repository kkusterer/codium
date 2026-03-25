from flask import Flask, request, render_template
import jinja2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("log_in_page.html")

@app.route("/login" ,  methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == "kaleb" and password == "123":
        return render_template("good_login.html")
    else:
        return render_template("failed_login.html")


@app.route("/submit_question",methods=["POST"])
def submit_question():
    question1 = request.form.get("question1", "")
    print("Question: " + question1)
    return render_template("good_login.html")
