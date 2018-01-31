from sqlalchemy import create_engine,Column,Integer,TEXT,ForeignKey,Boolean,DATE

from sqlalchemy.orm import relationship, sessionmaker, backref

from sqlalchemy.ext.declarative import declarative_base

from datetime import date

from uuid import uuid4


Model = declarative_base()


class Question(Model):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    url = Column(TEXT)
    lock = Column(Boolean)
    difficulty = Column(TEXT)
    python_solution = Column(TEXT)
    c_plus_plus_solution = Column(TEXT)

    daily_id = Column(TEXT,ForeignKey('daily.id'))
    daily = relationship("Daily", backref=backref('questions'))



class Daily(Model):
    __tablename__ = 'daily'
    id = Column(Integer,primary_key=True,autoincrement=True)
    date = Column(DATE, default=date.today())


engine = create_engine('sqlite:///daily.db', echo=True)

DBsession =sessionmaker(bind=engine)
session = DBsession()

Model.metadata.create_all(engine)
