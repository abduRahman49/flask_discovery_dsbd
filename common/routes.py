from flask import Blueprint, render_template


bp = Blueprint("common", __name__)


@bp.route("/")
@bp.route("/index")
@bp.route("/home")
def hello_world():
    # réponse HTTP à l'utilisateur
    return render_template("index.html")

@bp.route("/about/<name>")
def about(name):
    # réponse HTTP à l'utilisateur
    return render_template("about.html", name=name)

@bp.route("/contact")
def contact():
    # réponse HTTP à l'utilisateur
    nom ="Abdou"
    etudiant = {"nom": "Fall", "prenom": "Samba", "age": 21}
    liste_cours = ["Python", "Flask", "UML"]
    return render_template("contact.html", name=nom, student=etudiant, cours=liste_cours)