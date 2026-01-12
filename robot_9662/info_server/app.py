from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    form = request.form

    team_number   = form.get("team_number", "")
    team_name     = form.get("name_of_team", "")
    drive_type    = form.get("drive", "")
    can_climb     = form.get("ladder_climb", "")
    highest_rung  = form.get("rung", "")
    auto_score    = form.get("auto_score", "")
    auto_average  = form.get("auto_avg", "")
    primary_role  = form.get("role", "")

    print("\n--- Alliance Survey Submission ---")
    print(f"Team Number:      {team_number}")
    print(f"Team Name:        {team_name}")
    print(f"Drive Type:       {drive_type}")
    print(f"Can Climb:        {can_climb}")
    print(f"Highest Rung:     {highest_rung}")
    print(f"Auto Scoring:     {auto_score}")
    print(f"Avg Auto Score:   {auto_average}")
    print(f"Primary Role:     {primary_role}")
    print("----------------------------------\n")

    file_name = "info"
    file_extention = ".txt"
    file = file_name + file_extention
    mode ="a"
    try:
        with open(file, mode) as file:
            file.write("--- Alliance Survey Submission ---")
            file.write("\n")
            file.write(f"\n-----***** {team_number} *****-----")
            file.write("\n")
            file.write(f"\nTeam Number:      {team_number}")
            file.write(f"\nTeam Name:        {team_name}")
            file.write(f"\nDrive Type:       {drive_type}")
            file.write(f"\nCan Climb:        {can_climb}")
            file.write(f"\nHighest Rung:     {highest_rung}")
            file.write(f"\nAuto Scoring:     {auto_score}")
            file.write(f"\nAvg Auto Score:   {auto_average}")
            file.write(f"\nPrimary Role:     {primary_role}")
            file.write("\n----------------------------------\n")
            file.write("\n")  
            file.write("\n")
    except:
        ()

    return render_template("test.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
