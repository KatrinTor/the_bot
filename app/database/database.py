import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String)

    answers = relationship("AnswerInfo", back_populates="question")


class AnswerInfo(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

    question = relationship("Questions", back_populates="answers")
    user = relationship("Users", back_populates="answers")


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    answers = relationship("AnswerInfo", back_populates="user")


Base.metadata.create_all(engine)
