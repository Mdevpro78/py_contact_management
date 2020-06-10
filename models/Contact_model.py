from sqlalchemy import Column, String, Integer

from .Base import Base


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    gender = Column(String)

    def __init__(self, first_name, last_name, phone_number, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.gender = gender

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])[1:]

