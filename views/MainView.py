from tkinter import Frame, Button
from tkinter import BOTH
from tkinter import LEFT, RIGHT
from tkinter import SUNKEN


from views.TableView import TableView


class GUI:
    OPTIONS = {"fg" : '#0C120C',
               "font": ('bold', 13),
               "width": 15, "height": 2}

    def __init__(self, master, title):
        self.master = master
        self.master.geometry('885x500')
        self.master.title(f'{title}')

        self.buttons_frame = Frame(self.master, width = 150, bg = '#D3D4D9')
        self.buttons_frame.pack(side = LEFT, fill = BOTH, padx = 5, pady = 5)

        self.table = TableView(self.master, width = 450, relief = SUNKEN)
        self.table.pack(side = RIGHT, fill = BOTH, expand=True)

        self.create_main_columns()


    def create_main_columns(self):
        self.insert_button = Button(self.buttons_frame, text = 'Enter New',
                                    bg = '#01BAEF', **self.OPTIONS)
        self.delete_button = Button(self.buttons_frame, text = 'Delete',
                                    bg = '#EC0B43',**self.OPTIONS)
        self.update_button = Button(self.buttons_frame, text = 'Edite',
                                    bg = '#7AE7C7', **self.OPTIONS)

        self.insert_button.grid(row=0, column=0, padx=5, pady=5)
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)
        self.update_button.grid(row=2, column=0, padx=5, pady=5)
