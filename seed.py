from app import app
from extensions.sqlalchemy import db
from models import User, Profile, Homework, Session, SexeType, SessionType
from datetime import date, datetime, timedelta

# context manager
with app.app_context():
    db.session.execute(db.delete(Session))
    db.session.execute(db.delete(Homework))
    db.session.execute(db.delete(Profile))
    db.session.execute(db.delete(User))
    db.session.commit()

    #--Utilisateurs--------------------------------------------------------
    u1 = User(username="alice", password="hash1", is_active=True)
    u2 = User(username="bob", password="hash2", is_active=True)
    u3 = User(username="charlie", password="hash3", is_active=False)
    u4 = User(username="diana", password="hash4", is_active=True)
    u5 = User(username="carl", password="hash5", is_active=False)

    #--Correcteurs
    c1 = User(username="correcteur1", password="hash1", is_active=True)
    c2 = User(username="correcteur2", password="hash2", is_active=True)

    db.session.add_all([u1, u2, u3, u4, u5, c1, c2])
    db.session.flush() # obtenir les id sans commit

    #--Profils
    p1 = Profile(
        email="alice@yopmail.com",
        prenom="alice",
        nom="smith",
        date_of_birth=date.fromisoformat("2002-01-13"),
        telephone="777777777",
        sexe="F",
        user_id=u1.id
    )

    p2 = Profile(
        email="bob@yopmail.com",
        prenom="bob",
        nom="johnson",
        date_of_birth=date.fromisoformat("2001-04-20"),
        telephone="777777770",
        sexe="M",
        user_id=u2.id
    )

    p3 = Profile(
        email="charlie@yopmail.com",
        prenom="charlie",
        nom="davis",
        date_of_birth=date.fromisoformat("2000-05-15"),
        telephone="777777700",
        sexe="M",
        user_id=u3.id
    )

    p4 = Profile(
        email="diana@yopmail.com",
        prenom="diana",
        nom="robin",
        date_of_birth=date.fromisoformat("1999-06-10"),
        telephone="777777701",
        sexe="F",
        user_id=u4.id
    )

    p5 = Profile(
        email="carl@yopmail.com",
        prenom="carl",
        nom="jackson",
        date_of_birth=date.fromisoformat("1999-06-10"),
        telephone="777777702",
        sexe="M",
        user_id=u5.id
    )

    db.session.add_all([p1, p2, p3, p4, p5])

    # Homeworks
    h1 = Homework(
        title="Devoir Python",
        description="Examen POO Python",
        due_date=datetime.now() + timedelta(days=3),
        corrector=c1
    )

    h2 = Homework(
        title="Devoir Maths",
        description="Calcul différentiel",
        due_date=datetime.now() + timedelta(days=-1),
        corrected_by=c2.id
    )

    h3 = Homework(
        title="Devoir Anglais",
        description="Examen Anglais",
        due_date=datetime.now() + timedelta(days=1),
        corrected_by=c2.id
    )

    h4 = Homework(
        title="Devoir Droit",
        description="Examen Droit TIC",
        due_date=datetime.now() + timedelta(days=4),
        corrector=c1
    )

    db.session.add_all([h1, h2, h3, h4])

    s1 = Session(session_type=SessionType.NORMALE)
    s2 = Session(session_type=SessionType.RATTRAPAGE)

    s1.homeworks.extend([h1, h2])
    s2.homeworks.extend([h3, h4])

    db.session.add_all([s1, s2])

    db.session.commit()
