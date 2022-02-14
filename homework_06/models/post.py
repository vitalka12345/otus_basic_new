from sqlalchemy import Column, Integer, String
from .database import db


class Posts(db.Model):
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, nullable=True, default=0)
    title = Column(String, nullable=True, default="")
    body = Column(String, nullable=True, default="")
