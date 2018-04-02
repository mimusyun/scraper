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
