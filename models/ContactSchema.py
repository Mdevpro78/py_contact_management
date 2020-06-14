from sqlalchemy import Column, String, Integer

from .Base import Base


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    gender = Column(String)

    def __init__(self, first_name=None, last_name=None, phone_number=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.gender = gender


    def info(self):
        return {'Firstname': self.first_name ,'Lastname': self.last_name,
                'Phone': self.phone_number, 'Gender': self.gender, 'id': self.id}


