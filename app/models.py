from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    size = Column(Integer)
    upload_time = Column(DateTime)
    s3_url = Column(String)
