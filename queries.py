from app import app
from extensions.sqlalchemy import db
from sqlalchemy import select , func , and_ , or_ , not_ , desc , asc
from models import User, Profile, Homework, Session, SexeType, SessionType
from datetime import date, datetime, timedelta, timezone

# context manager
with app.app_context():
    # Question 1
    all_users_stmt = select(User.id, User.username, User.is_active)
    result1 = db.session.execute(all_users_stmt).all()
    print("all users: ", result1)

    # Question 2
    # ref helper.functions

    # Question 3
    active_users_stmt = select(User).where(User.is_active).order_by(User.username)
    result2 = db.session.execute(active_users_stmt).scalars().all()
    print("active users: ", result2)

    # Question 4
    total_active_users_stmt = select(func.count(User.id)).where(User.is_active)
    result3 = db.session.execute(total_active_users_stmt).scalar()
    print("count users: ", result3)

    # Question 5
    first_user_stmt = select(User).order_by(asc(User.created_at)).limit(1)
    result4 = db.session.execute(first_user_stmt).scalar()

    last_user_stmt = select(User).order_by(desc(User.created_at)).limit(1)
    result5 = db.session.execute(first_user_stmt).scalar()
    print("first user and last user: ", result4, result5)

    # Question 6
    filtered_users_by_name_stmt = select(User).where(User.username.ilike("%a%"))
    result6 = db.session.execute(filtered_users_by_name_stmt).scalars().all()
    print("usernames containing a: ", result6)

    # Question 7
    active_users_starting_with_a_or_b_stmt = select(User).where(
        and_(
            User.is_active,
            or_(
                User.username.ilike("a%"),
                User.username.ilike("b%")
            )
        )
    )
    result7 = db.session.execute(active_users_starting_with_a_or_b_stmt).scalars().all()
    print("active users with names a or b: ", result7)

    # Question 8
    feminin_profiles_stmt = select(Profile).where(Profile.sexe != SexeType.M)
    result8 = db.session.execute(feminin_profiles_stmt).scalars().all()
    print("feminine profiles: ", result8)

    # Question 9
    current_date = datetime.now(timezone.utc)
    passed_homeworks_stmt = select(Homework).where(Homework.due_date <= current_date)
    result9 = db.session.execute(passed_homeworks_stmt).scalars().all()
    print("passed homeworks: ", result9)

    # Question 10
    start_date = date.fromisoformat("1995-01-01")
    end_date = date.fromisoformat("2000-12-31")
    profiles_born_between_two_dates_stmt = select(Profile).where(Profile.date_of_birth.between(start_date, end_date))
    result10 = db.session.execute(profiles_born_between_two_dates_stmt).scalars().all()
    print("profiles between two dates: ", result10)

    # Question 11
    internal_join_user_profile_stmt = select(User.username, Profile.prenom, Profile.nom).join(Profile, User.id == Profile.user_id)
    result11 = db.session.execute(internal_join_user_profile_stmt).scalars().all()
    print("internal join: ", result11)

    # Question 12

    external_join_user_profile_stmt = select(User.username, Profile.email).join(Profile, User.id == Profile.user_id, isouter=True)
    result12 = db.session.execute(external_join_user_profile_stmt).scalars().all()
    print("external join: ", result12)

