from tkinter import Tk, Frame, Button
from tkinter import BOTH
from tkinter import LEFT, RIGHT
from tkinter import SUNKEN

from views.FormView import FormView
from views.TableView import TableView


class GUI:
    OPTIONS = {"fg" : '#0C120C',
               "font": ('bold', 13),
               "width":15, "height":2}
    def __init__(self, master, title):
        self.master = master
        self.master.geometry('885x500')
        self.master.resizable(width=False, height=False)
        self.master.title(f'{title}')

        self.buttons_frame = Frame(self.master, width=150, bd=1, bg='#D3D4D9')
        self.buttons_frame.pack(side=LEFT, fill=BOTH, padx=5, pady=5)

        self.table = TableView(self.master, width=450, relief=SUNKEN)
        self.table.tree['columns'] = ['1', '2', '3', '4']
        self.table.create_columns(*self.table.tree['columns'])
        self.table.pack(side=RIGHT, fill=BOTH)


        self.create_main_columns()

    def create_main_columns(self):
        self.insert_button = Button(self.buttons_frame, text = 'Enter New',
                                    bg = '#01BAEF', **self.OPTIONS,
                                    command = self.create_insert_form)
        self.delete_button = Button(self.buttons_frame, text = 'Delete',
                                    bg = '#EC0B43',**self.OPTIONS)
        self.update_button = Button(self.buttons_frame, text = 'Edite',
                                    bg = '#7AE7C7', **self.OPTIONS,
                                    command = self.create_update_form)

        self.insert_button.grid(row=0, column=0, padx=5, pady=5)
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)
        self.update_button.grid(row=3, column=0, padx=5, pady=5)

    def create_insert_form(self):
        tk = Tk()
        self.insert_form = FormView(tk, 'Enter New Contact')
        self.insert_form.pack()
        tk.mainloop()

    def create_update_form(self):
        tk = Tk()
        self.update_form = FormView(tk, 'Update Current Contact')
        self.update_form.submit_btn.config(text='Update')
        self.update_form.pack()
        tk.mainloop()

if __name__ == '__main__':
    root = Tk()
    app = GUI(root, 'test')
    root.mainloop()
