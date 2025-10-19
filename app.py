from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

app = Flask(__name__)
app.secret_key = "devkey"  # necessaria per i messaggi flash

# === HOMEPAGE ===


@app.route("/")
def home():
    try:
        with open("projects.json", "r", encoding="utf-8") as f:
            projects = json.load(f)
        preview_projects = projects[:3]
    except Exception as e:
        print("Errore nel caricamento dei progetti:", e)
        preview_projects = []
    return render_template("home.html", projects=preview_projects)



# === PAGINA PROGETTI ===
@app.route("/progetti")
def show_projects():
    try:
        with open("projects.json", "r", encoding="utf-8") as f:
            projects = json.load(f)
    except Exception as e:
        projects = []
        print("Errore nel caricamento dei progetti:", e)
    return render_template("projects.html", projects=projects)

# === PAGINA SKILLS ===
@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact")
def contact():
    return "<h1>Pagina contatti in costruzione</h1>"
@app.route("/about")
def about():
    return render_template("about.html")

# === AVVIO APP ===
if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)
