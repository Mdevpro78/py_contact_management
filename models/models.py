from abc import ABC

from models.Contact_schema import Contact
from models.Base import Base, Session, engine


class AbstactModel(ABC):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    
class ContactModel(AbstactModel):

    def insert_contact(self, **kwargs):
        self.session.add(Contact(**kwargs))
        self.session.commit()

    def delete_contact(self, contact_id):
        self.session.delete(
            self.session.query(Contact).filter(Contact.id == contact_id).first()
        )
        self.session.commit()

    def update_contact(self, contact_id, **kwargs):
        self.session.query(Contact).filter(Contact.id == contact_id).update(kwargs)
        self.session.commit()

    def read_contact(self, contact_id):
        return self.session.query(Contact).get(contact_id)

    @property
    def read_all_contact(self):
        return self.session.query(Contact).all()
