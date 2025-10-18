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
        return render_template("home.html", projects=preview_projects)
    except Exception as e:
        return f"<h1>Errore interno:</h1><pre>{e}</pre>"


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

# === PAGINA CONTATTI ===
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nome = request.form.get("nome")
        cognome=request.form.get("cognome")
        email = request.form.get("email")
        messaggio = request.form.get("messaggio")

        if not nome or not email or not messaggio:
            flash("Tutti i campi sono obbligatori.", "error")
            return redirect(url_for("contact"))

        data = {"nome": nome,"cognome": cognome,"email": email, "messaggio": messaggio}

        if not os.path.exists("messages.json"):
            with open("messages.json", "w", encoding="utf-8") as f:
                json.dump([], f)

        with open("messages.json", "r+", encoding="utf-8") as f:
            messaggi = json.load(f)
            messaggi.append(data)
            f.seek(0)
            json.dump(messaggi, f, indent=4, ensure_ascii=False)

        flash("Messaggio inviato con successo!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")
@app.route("/about")
def about():
    return render_template("about.html")

# === AVVIO APP ===
if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)
