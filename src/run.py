from sqlalchemy import create_engine, Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Job(Base):
    __tablename__ = 'job_ads'
    id = Column(Integer, primary_key=True)
    uid = Column(Text)
    title = Column(Text)


def init_db(db_uri):
    """
    Drop all existing tables
    Create table for job ads
    """
    engine = create_engine(db_uri)
    metadata.drop_all(engine)
    metadata.create_all(engine)


def main():

    db_uri = 'postgres://test:testpass@db:5432/heyjobs'
    # target_url = 'https://www.heyjobs.de/en/jobs-in-berlin'

    # initialize db
    init_db(db_uri)


if __name__ == '__main__':
    main()
