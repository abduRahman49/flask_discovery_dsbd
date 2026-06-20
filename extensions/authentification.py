from flask_login import LoginManager
from models import User
from .sqlalchemy import db

# instanciation de l'extension Flask Login
login_manager = LoginManager()

# Permet charger l'utilisateur sur l'application
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
