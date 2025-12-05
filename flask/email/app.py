from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    print("\n[Login Attempt]")
    print("Username:", username)
    print("Password:", password)

    if username == "kkusterer@admin.gmail.com" and password == "admin123":
        print("admin entered" "\n")
        return render_template("admin_login.html")

    else:
        print("default entry" "\n")
        return render_template("default_login.html")

if __name__ == "__main__":
    print("Flask server running at http://localhost:5000")
    app.run(debug=True)
