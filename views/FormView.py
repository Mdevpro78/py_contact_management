from tkinter import (Tk, Label, Entry,
                     Radiobutton, Button,
                     Frame)

from tkinter import StringVar


class ContactInformation:
    def __init__(self):
        self.name = StringVar()
        self.last_name = StringVar()
        self.gender = StringVar()
        self.phone_number = StringVar()

    @staticmethod
    def get_attributes():
        return 'Name', 'Last Name', 'Gender', 'Phone Number'

    def informaion(self):
        return {'name':self.name.get(), 'last_name': self.last_name.get(),
                'gender': self.gender.get(), 'phone_number': self.phone_number.get()}


class FormView:

    def __init__(self, title):
        self.window = Tk()
        self.window.configure(background='#96C3CE')
        self.contact = ContactInformation()
        self.window.title(f'{title}')
        self.window.geometry('500x500')
        self.window_title = Label(self.window, text='Contact Form',
                                  width=20, font=("bold", 20))
        self.window_title.place(x=90, y=53)
        self.create_labels()
        self.create_entries()
        self.create_radiobuttons()
        self.create_buttons()
        self.window.mainloop()

    def create_entries(self):
        Entry(self.window, textvariable = self.contact.name).place(x = 240, y = 130)
        Entry(self.window, textvariable = self.contact.last_name).place(x = 240, y = 180)
        Entry(self.window, textvariable = self.contact.phone_number).place(x = 240, y = 230)

    def create_labels(self):
        frame = Frame(self.window, width=100, height=140, bg='#96C3CE')
        for index, item in enumerate(self.contact.get_attributes()):
            lbl = Label(frame, text=f"{item}: ", width=14, font=("bold", 10), bg='#96C3CE', anchor='w')
            lbl.grid(row=index, column=0, pady=13.5)
        frame.place(x=120, y=115)

    def create_radiobuttons(self):
        Radiobutton(self.window, text = "Male", padx = 5, variable = self.contact.gender,
                    value = "Male", bg='#96C3CE').place(x = 235, y = 280)
        Radiobutton(self.window, text = "Female",padx = 5, variable = self.contact.gender,
                    value = "Female", bg='#96C3CE').place(x = 300, y = 280)

    def create_buttons(self):
        submit_btn = Button(self.window, text = 'Submit', width = 20, bg = '#58A4B0',
                            fg = '#020100', font = ('bold', 11))
        submit_btn.place(x = 255, y = 350)
        submit_btn.config(command=self.contact.informaion)

        Button(self.window, text = 'Cancell', width = 20, bg = '#D64933', command=self.window.destroy,
               fg = '#020100', font = ('bold', 11)).place(x = 55, y = 350)



# contact = FormView('ContactInformation')