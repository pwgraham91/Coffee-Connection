import datetime
import sqlalchemy
from sqlalchemy import orm
from faker import Faker

from app.models import User
from config_director import Config


def create_test_users(session):
    fake = Faker()

    for i in range(50):
        person = User(
            name=fake.name(),
            email=fake.email(),
            created_at=datetime.datetime.utcnow()
        )
        session.add(person)

    session.commit()


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
    Session = orm.sessionmaker(bind=engine)
    session = Session()
    create_test_users(session)
