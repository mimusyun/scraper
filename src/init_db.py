from sqlalchemy import create_engine, Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from run import load_config


Base = declarative_base()
metadata = Base.metadata
table_name = load_config()['app']['table_name']


class Job(Base):
    __tablename__ = table_name
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
