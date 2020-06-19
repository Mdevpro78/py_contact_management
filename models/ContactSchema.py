from sqlalchemy import Column, String, Integer

from .Base import Base


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    gender = Column(String)

    @property
    def informations(self):
        return {'Firstname': self.first_name ,'Lastname': self.last_name,
                'Phone': self.phone_number, 'Gender': self.gender}


