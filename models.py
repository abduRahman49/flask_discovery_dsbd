import enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, DateTime, Enum, Table, Column, Date
from datetime import datetime, timezone, date
from extensions.sqlalchemy import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


## ======== Centralisation de tous les modèles de l'application sur ce module ======= ##

class SessionType(enum.Enum):
    NORMALE = "NORMALE"
    RATTRAPAGE = "RATTRAPAGE"


class SexeType(enum.Enum):
    M = "M"
    F = "F"


session_homework = Table(
    "session_homework",
    db.metadata,
    Column("homework_id", db.ForeignKey("homework.id"), primary_key=True),
    Column("session_id", db.ForeignKey("session.id"), primary_key=True)
)

# UserMixin fourni des attributs et des méthodes dont Flask-Login a besoin
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    profile: Mapped["Profile"] = db.relationship(back_populates="user", uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Profile(db.Model):
    __tablename__ = 'profile'
    id: Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str] = mapped_column(String(150), unique=True)
    nom: Mapped[str] = mapped_column(String(150))
    prenom: Mapped[str] = mapped_column(String(150))
    date_of_birth: Mapped[date] = mapped_column(Date)
    telephone: Mapped[str] = mapped_column(String(20))
    sexe: Mapped[SexeType] = mapped_column(Enum(SexeType))
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), unique=True)
    user: Mapped["User"] = db.relationship(back_populates="profile")


class Homework(db.Model):
    __tablename__ = 'homework'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    corrected_by: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=True)
    corrector: Mapped['User'] = db.relationship('User', backref='homeworks_to_correct')
    sessions : Mapped[list["Session"]] = db.relationship(secondary=session_homework, back_populates="homeworks")


class Session(db.Model):
    __tablename__ = "session"
    id : Mapped[int] = mapped_column(primary_key=True)
    session_type : Mapped[SessionType] = mapped_column(Enum(SessionType))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    homeworks : Mapped[list[Homework]] = db.relationship(secondary=session_homework, back_populates="sessions")
