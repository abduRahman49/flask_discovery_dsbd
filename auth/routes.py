from flask import Blueprint, render_template, request
from models import User
from extensions.sqlalchemy import db


bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print("Username: ", username)
    print("Password: ", password)
    return render_template("login.html")


@bp.route("/register")
def register():
    # recupération des infos de l'utilisateur
    username = request.form.get("username")
    password = request.form.get("password")

    user = User(username)
    user.set_password(password)
    db.session.add(user)
    db.session.flush()


    # recupération des infos du profil
    email = request.form.get("email")
    prenom = request.form.get("prenom")
    nom = request.form.get("nom")
    sexe = request.form.get("sexe")
    telephone = request.form.get("telephone")
    date_of_birth = request.form.get("date_of_birth")
