from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["Post"] )
def submit():
    team_number = request.form.get("team_number", "")
    name_of_team =  request.form.get("name_of_team", "")
    drive_type = request.form.get("drive", "")

    print("team number:", team_number)
    print("team name:", name_of_team)
    print("drive type:", drive_type)
    return render_template("test.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)