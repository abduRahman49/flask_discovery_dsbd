from sqlalchemy import select
from models import User
from extensions.sqlalchemy import db


def get_user_by_username(username):
    stmt = select(User).where(User.username == username)
    result = db.session.execute(stmt).scalar()
    return result
