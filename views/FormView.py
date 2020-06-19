from tkinter import (Label, Entry,
                     Toplevel,
                     Button, Frame)

from tkinter import StringVar, IntVar

from tkinter.ttk import Combobox


class ContactView:
    def __init__(self):
        self.id = IntVar()
        self.name = StringVar()
        self.last_name = StringVar()
        self.gender = StringVar()
        self.phone_number = StringVar()

    @staticmethod
    def get_attributes():
        return 'Name', 'Last Name', 'Phone Number', 'Gender'

    def set_values(self, **kwargs):
        self.name.set(kwargs['Firstname'])
        self.last_name.set(kwargs['Lastname'])
        self.phone_number.set(kwargs['Phone'])
        self.gender.set(kwargs['Gender'])


class FormView(Toplevel):
    OPTIONS = {'font': ('bold', 11)}
    def __init__(self, parent, title):
        super().__init__(parent)
        self.resizable(width = False, height = False)
        self.configure(background = '#96C3CE')
        self.title(f'{title}')
        self.geometry('500x500')

        self.contact = ContactView()
        self.window_title = Label(self, text = 'Contact Form',
                                  width = 20, font = ("bold", 20))
        self.window_title.place(x = 90, y = 53)

        self.create_labels()
        self.create_entries()
        self.create_combobox()
        self.create_buttons()


    def create_entries(self):
        self.name_entry = Entry(self, textvariable = self.contact.name,
                                text = self.contact.name, **self.OPTIONS)
        self.name_entry.place(x = 240, y = 130)

        self.last_name_entry = Entry(self,
                                     textvariable = self.contact.last_name,
                                     text = self.contact.last_name, **self.OPTIONS)
        self.last_name_entry.place(x = 240, y = 180)

        self.phone_nubmer_entry = Entry(self,
                                        textvariable = self.contact.phone_number,
                                        text = self.contact.phone_number, **self.OPTIONS)
        self.phone_nubmer_entry.place(x = 240, y = 230)


    def create_labels(self):
        frame = Frame(self, width = 100, height = 140, bg = '#96C3CE')
        for index, item in enumerate(self.contact.get_attributes()):
            lbl = Label(frame, text = f"{item}: ", width = 14,
                        bg = '#96C3CE', anchor = 'w', **self.OPTIONS)
            lbl.grid(row = index, column = 0, pady = 13.5)
        frame.place(x = 120, y = 115)


    def create_combobox(self):
        self.contact_gender = ['Female', 'Male']
        self.gender = Combobox(self, values = self.contact_gender, **self.OPTIONS)
        self.gender.config(width = 17)
        self.gender.current(0)
        self.gender.place(x = 238, y = 280)


    def create_buttons(self):
        self.submit_btn = Button(self, text = 'Submit',
                                 width = 20, bg = '#58A4B0',
                                 fg = '#020100', **self.OPTIONS)
        self.submit_btn.place(x = 255, y = 350)

        Button(self, text = 'Cancell', width = 20,
               bg = '#D64933', command = self.destroy,
               fg = '#020100', **self.OPTIONS).place(x = 55, y = 350)


    @property
    def get_entries_values(self):
        return {'first_name': self.name_entry.get(), 'last_name': self.last_name_entry.get(),
                'phone_number': self.phone_nubmer_entry.get(), 'gender': self.gender.get()}
