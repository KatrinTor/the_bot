import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.tables import AnswerInfo

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))


def add_question_answer(question_id, answer_text):
    Session = sessionmaker(bind=engine)
    session = Session()
    answer = AnswerInfo(question_id=question_id, answer=answer_text)
    session.add(answer)
    session.commit()
