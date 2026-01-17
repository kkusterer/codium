from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("survey.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_number TEXT,
            team_name TEXT,
            drive_type TEXT,
            can_climb TEXT,
            highest_rung TEXT,
            auto_score TEXT,
            auto_average TEXT,
            primary_role TEXT,
            pit_num TEXT
        )
    """)
    conn.commit()
    conn.close()

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
    pit_num = form.get("pit_number", "")

    print("\n--- Alliance Survey Submission ---")
    print(f"Team Number:      {team_number}")
    print(f"Team Name:        {team_name}")
    print(f"Drive Type:       {drive_type}")
    print(f"Can Climb:        {can_climb}")
    print(f"Highest Rung:     {highest_rung}")
    print(f"Auto Scoring:     {auto_score}")
    print(f"Avg Auto Score:   {auto_average}")
    print(f"Primary Role:     {primary_role}")
    print(f"Pit number:       {pit_num}")
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
            file.write(f"\nTeam Number: {team_number}") 
            file.write(f"\nTeam Name: {team_name}") 
            file.write(f"\nDrive Type: {drive_type}") 
            file.write(f"\nCan Climb: {can_climb}") 
            file.write(f"\nHighest Rung: {highest_rung}") 
            file.write(f"\nAuto Scoring: {auto_score}") 
            file.write(f"\nApit_numvg Auto Score: {auto_average}") 
            file.write(f"\nPrimary Role: {primary_role}") 
            file.write(f"\nPit number:       {pit_num}")
            file.write("\n----------------------------------\n") 
            file.write("\n") 
            file.write("\n") 
    except: ()

    conn = sqlite3.connect("survey.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO responses (
            team_number, team_name, drive_type, can_climb,
            highest_rung, auto_score, auto_average, primary_role, pit_num
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        team_number, team_name, drive_type, can_climb,
        highest_rung, auto_score, auto_average, primary_role, pit_num
    ))
    conn.commit()
    conn.close()

    return render_template("test.html")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
