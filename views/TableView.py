from tkinter import Scrollbar, Frame
from tkinter import LEFT, RIGHT
from tkinter import YES, NO
from tkinter import Y, BOTH

from tkinter.ttk import Treeview


class TableView(Frame):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.tree = Treeview(self, selectmode='browse')
        self.tree.column("#0", width=100, minwidth=75, stretch=NO)
        self.tree.heading("#0", text='row', anchor='center')
        self.scroll = Scrollbar(self, command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.tree.pack(expand=True, side=LEFT, fill=BOTH)


    def create_columns(self, *columns):
        for column in columns:
            self.tree.column(f"{column}", width=150, minwidth=150, stretch=YES)

    def create_heading(self, *columns):
        for index, column in enumerate(columns):
            self.tree.heading(f"#{index+1}", text=f"{column}", anchor='center')

    def fill_row(self, *args):
        for index, contact in enumerate(args):
            self.tree.insert("", 'end', f"{contact.id}", text=f"{index}", values=list(contact.info().values()))
