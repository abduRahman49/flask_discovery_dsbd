from helper.exceptions import UserAlreadyExists, UserDoesNotExistException, IncorrectPasswordExcpetion
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from services.authentification import AuthentificationService
from models import User, Profile
from extensions.sqlalchemy import db
from sqlalchemy import select
from datetime import date


bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form.get("username")
    password = request.form.get("password")

    AuthentificationService.connect_user(username, password)
    return redirect(url_for("common.hello_world"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # recupération des infos de l'utilisateur
    username = request.form.get("username")
    password = request.form.get("password")

    stmt = select(User).where(User.username == username)
    user_in_database = db.session.execute(stmt).scalar_one_or_none()
    if user_in_database:
        raise UserAlreadyExists("Utilisateur avec ce username existe déjà")


    user = User(username=username)
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
    formatted_date_of_birth = date.fromisoformat(date_of_birth)
    profile = Profile(
        email=email,
        prenom=prenom,
        nom=nom,
        sexe=sexe,
        telephone=telephone,
        date_of_birth=formatted_date_of_birth,
        user_id=user.id
    )

    db.session.add(profile)
    db.session.commit()
    return redirect(url_for("auth.login"))


@bp.route("/logout")
def log_out():
    logout_user()
    return redirect(url_for("auth.login"))