from app import app
from extensions.sqlalchemy import db
from sqlalchemy import select, func, and_, or_, not_, desc, asc
from datetime import datetime, timezone
from models import User


with app.app_context():
    # Question 1
    stmt = select(User.id, User.username, User.is_active)
    users = db.session.execute(stmt).all()
    print("L'ensemble des utilisateurs ", users)
