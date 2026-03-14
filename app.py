# import de la bibliotheque Flask et des fonctions utilitaires
import json
from flask import Flask, render_template
from extensions.sqlalchemy import db
from .models import User

# définition de l'instance de l'application
app = Flask(__name__)
# configuration de l'application à partir du fichier config.json
app.config.from_file("config.json", load=json.load)

# initialisation de l'extension SQLAlchemy
db.init_app(app)

with app.app_context():
    db.create_all()

# liaison entre une route (url) de l' application et un controleur (fonction)
# lien entre url et fonction
@app.route("/")
@app.route("/index")
@app.route("/home")
def hello_world():
    # réponse HTTP à l'utilisateur
    return render_template("index.html")

@app.route("/about/<name>")
def about(name):
    # réponse HTTP à l'utilisateur
    return render_template("about.html", name=name)

@app.route("/contact")
def contact():
    # réponse HTTP à l'utilisateur
    nom ="Abdou"
    etudiant = {"nom": "Fall", "prenom": "Samba", "age": 21}
    liste_cours = ["Python", "Flask", "UML"]
    return render_template("contact.html", name=nom, student=etudiant, cours=liste_cours)

@app.route("/filtrage")
def filtrage():
    posts = [
        {"title": "Flask Intro", "views": 1243.567},
        {"title": "Jinja Deep Dive", "views": 987.3},
        {"title": "", "views": 0}
    ]
    titres = [post["title"] for post in posts]
    return render_template("filtre.html", publications=posts, titres=titres)

@app.route("/iteration")
def iteration():
    posts = [
        {"title": "Flask Intro", "views": 1243.567},
        {"title": "Jinja Deep Dive", "views": 987.3},
        {"title": "", "views": 0}
    ]
    return render_template("boucle.html", posts=posts)
