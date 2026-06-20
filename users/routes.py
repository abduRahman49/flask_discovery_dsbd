from flask import Blueprint, render_template
from flask_login import login_required
from extensions.sqlalchemy import db
from sqlalchemy import select
from models import User, Profile


bp = Blueprint("users", __name__)

@bp.route("/users")
@login_required
def list_users():
    stmt = select(User).where(User.is_active).order_by(User.username)
    users = db.session.execute(stmt).scalars().all()
    return render_template("users.html", users=users)


@bp.route("/profil/<id>")
@login_required
def profil(id):
    stmt = select(Profile).where(Profile.id == id)
    profile = db.session.execute(stmt).scalar()
    return render_template("profile.html", profil=profile)
