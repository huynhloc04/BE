
import os
from sqlmodel import SQLModel, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv



ACCESS_TOKEN_EXPIRE_MINUTES = 500
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
DATABASE_URL = os.environ.get("DATABASE_URL")

JD_SAVED_DIR = "static/job/uploaded_jds"
CV_SAVED_DIR = "static/resume/cv/uploaded_cvs"
CV_PARSE_PROMPT = "src/postjob/resources/prompts/cv_parsing.txt"
JD_PARSE_PROMPT = "src/postjob/resources/prompts/jd_parsing.txt"
MATCHING_PROMPT = "src/postjob/resources/prompts/matching.txt"
OPENAI_MODEL = "gpt-3.5-turbo-16k"
CV_EXTRACTION_PATH = "static/resume/cv/extracted_cvs"
JD_EXTRACTION_PATH = "static/job/extracted_jds"
EDITED_JOB = "static/job/edited_jobs"
CANDIDATE_AVATAR_DIR = "static/resume/avatar"
SAVED_TEMP = "static/resume/cv/temp"
MATCHING_DIR = "static/matching"
JD_SAVED_TEMP_DIR = "static/job/temp"
CV_SAVED_TEMP_DIR = "static/resume/cv/temp"
PAYMENT_DIR = 'static/payment/user_trans'

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")


class DatabaseSession:

    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def init(self):
        self.engine = create_engine(DATABASE_URL, echo=True)
        
    def create_all(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session

    def commit_rollback(self, session: Session):
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

db = DatabaseSession()