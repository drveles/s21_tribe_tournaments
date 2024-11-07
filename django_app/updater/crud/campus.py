from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


DATABASE_USER = "your_user"
DATABASE_PASSWORD = "your_password"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"
DATABASE_NAME = "postgres"

BASE_URL = f"postgresql://{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(BASE_URL)

with engine.connect() as connection:
    result = connection.execute("SELECT version();")
    print(result.fetchone())


def create_or_update_campus(name: str) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()

    existing_campus = session.query(Campuses).filter_by(name=name).first()
    if existing_campus:
        existing_campus.slug = name.lower()
    else:
        new_campus = Campuses(name=name, slug=name.lower())
        session.add(new_campus)

    session.commit()
    session.close()  # Закрываем сессию после завершения работы

    return True


if __name__ == "__main__":
    create_or_update_campus("Kazan")
