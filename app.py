from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["university_db"]
collection = db["faculty_info"]

# Route for homepage and form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        designation = request.form["designation"]
        emp_id = int(request.form["emp_id"])
        domains = request.form["domains"].split(",")
        email = request.form["email"]
        max_teams = int(request.form["max_teams"])
        total_batches = int(request.form["total_batches"])
        
        # Save data to MongoDB
        faculty_data = {
            "Name": name,
            "Designation": designation,
            "EMP_ID": emp_id,
            "Domains": [domain.strip() for domain in domains],
            "University_Email_ID": email,
            "Max_Teams": max_teams,
            "Total_Batches": total_batches,
        }
        collection.insert_one(faculty_data)
        flash("Faculty information added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("index.html")

# Route to display all faculty data
@app.route("/display")
def display():
    data = list(collection.find())
    return render_template("display.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
