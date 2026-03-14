from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, DateTime
from datetime import datetime, timezone
from extensions.sqlalchemy import db

## ======== Centralisation de tous les modèles de l'application sur ce module ======= ##


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(120))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)