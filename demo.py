from flask import Flask, render_template,request, redirect, url_for
import sqlite3

app = Flask(__name__)
def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
create_database()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/About")
def About():
    return render_template("About.html")


@app.route("/Service")
def Service():
    return render_template("Service.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO feedback(name,email,phone,message)
            VALUES(?,?,?,?)
        """,(name,email,phone,message))
        conn.commit()
        conn.close()
        return redirect(url_for("contact"))
    return render_template("contact.html")


@app.route("/software")
def software():
    return render_template("software.html")


@app.route("/cyber-security")
def cyber():
    return render_template("cyber.html")

@app.route("/Portfolio")
def Portfolio():
    return render_template("Portfolio.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")
@app.route("/tai")
def ai():
    return render_template("ai.html")
@app.route("/feedback")

def feedback():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    conn.close()
    return render_template("feedback.html", feedbacks=data)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)