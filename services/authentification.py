

from flask_login import login_user
from sqlalchemy import select
from extensions.sqlalchemy import db

from helper.exceptions import IncorrectPasswordExcpetion, UserDoesNotExistException
from models import User


class AuthentificationService:

    @classmethod
    def register_user():
        # code permettant de créar un utilisateur
        ...

    @classmethod
    def connect_user(username, password):
        # code permettant de connecter un utilisateur
        stmt = select(User).where(User.username == username)
        user_in_database = db.session.execute(stmt).scalar_one_or_none()
        if not user_in_database:
            raise UserDoesNotExistException("Utilisateur avec ce username n'existe pas")

        if not user_in_database.check_password(password):
            raise IncorrectPasswordExcpetion("Mot de passe incorrecte")

        login_user(user_in_database)

    @classmethod
    def deconnect_user():
        # code permettant de déconnecter un utilisateur
        ...
