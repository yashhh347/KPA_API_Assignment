from sqlalchemy import Column, Integer, String
from database import Base

class PersonalDetails(Base):
    __tablename__ = "personal_details"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
