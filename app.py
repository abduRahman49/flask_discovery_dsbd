# import de la bibliotheque Flask et des fonctions utilitaires
from flask import Flask, render_template

# définition de l'instance de l'application
app = Flask(__name__)

# liaison entre une route (url) de l' application et un controleur (fonction)
# lien entre url et fonction
@app.route("/")
@app.route("/index")
@app.route("/home")
def hello_world():
    # réponse HTTP à l'utilisateur
    return "Hello, World!"

@app.route("/about")
def about():
    # réponse HTTP à l'utilisateur
    return "<p>Hello, about!</p>"

@app.route("/contact")
def contact():
    # réponse HTTP à l'utilisateur
    nom ="Abdou"
    etudiant = {"nom": "Fall", "prenom": "Samba", "age": 21}
    liste_cours = ["Python", "Flask", "UML"]
    return render_template("contact.html", name=nom, student=etudiant, cours=liste_cours)
