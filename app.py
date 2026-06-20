# import de la bibliotheque Flask et des fonctions utilitaires
import json
from extensions.sqlalchemy import db
from extensions.migrations import migrate
from extensions.authentification import login_manager
from flask import Flask
from auth.routes import bp as auth_bp
from common.routes import bp as common_bp
from users.routes import bp as users_bp


# définition de l'instance de l'application
app = Flask(__name__)
# configuration de l'application à partir du fichier config.json
app.config.from_file("config.json", load=json.load)

# initialisation de l'extension SQLAlchemy
db.init_app(app)
# initialisation de l'extension Flask-Migrate
migrate.init_app(app, db)
# initialisation de l'extension Flask-Login
login_manager.init_app(app)
# Configuration de la route par défaut pour la page de connexion
login_manager.login_view = "auth.login"
login_manager.login_message = "Veuillez vous connecter ."

# Connecter les blueprints des différents modules à l'instance de l'app
app.register_blueprint(auth_bp)
app.register_blueprint(common_bp)
app.register_blueprint(users_bp)

### Module principal ###

# liaison entre une route (url) de l' application et un controleur (fonction)
# lien entre url et fonction


### Module de gestion des utilisateurs ###

