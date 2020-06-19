from tkinter import Tk

from models.ContactModel import ContactModel
from models.ContactModel import Contact

from views.MainView import GUI
from views.FormView import FormView
from views.MessageView import Message


class Controller(Tk):
    def __init__(self):
        super().__init__()
        self.contact = Contact()
        self.model = ContactModel()
        self.message = Message()
        self.gui = GUI(self, 'Contact Management')
        self.selected = None

        self.gui.table.tree['columns'] = list(self.contact.informations.keys())
        self.gui.table.tree.bind('<<TreeviewSelect>>', self.set_selected_item)

        self.gui.table.create_columns(*self.gui.table.tree['columns'])
        self.gui.table.create_heading(*self.gui.table.tree['columns'])

        self.gui.delete_button.config(command=self.delete_command)
        self.gui.insert_button.config(command=self.new_item_command)
        self.gui.update_button.config(command=self.update_command)

        self.update_gui_table()


    def update_gui_table(self):
        if len(self.model.read_all_contact):
            self.gui.table.fill_row(*self.model.read_all_contact)
        else:
            return

    def set_selected_item(self, event):
        self.selected = event.widget.selection()[0]

    def delete_command(self):
        if self.selected:
            if self.message.commit('Delete', 'Are you sure you want to delete the selected item?').conjugate():
                self.model.delete_contact(self.selected)
                self.gui.table.tree.delete(self.selected)
                self.selected = None
                self.update_gui_table()
        else:
            self.message.warning('warrning', 'Please select an item from list')

    def new_item_command(self):
        self.insert_form = FormView(self, 'Enter New Contact')
        self.insert_form.grab_set()
        self.insert_form.submit_btn.config(command=self.new_item_submit_btn_command)

    def new_item_submit_btn_command(self):
        if all(self.insert_form.get_entries_values.values()):
            if self.message.commit('Save', 'Are you save this?').conjugate():
                self.model.insert_contact(**self.insert_form.get_entries_values)
                self.update_gui_table()
                self.message.info('Submit', 'Your item added to list with success')
                self.insert_form.destroy()
            else:
                self.insert_form.destroy()
        else:
            self.message.warning('Input incorecct', 'Please fill all of the entries')

    def update_command(self):
        if self.selected:
            self.update_form = FormView(self, 'Update Contact')
            self.update_form.grab_set()
            self.update_form.contact.set_values(**self.model.read_contact(self.selected).informations)
            self.update_form.gender.current(self.update_form.contact_gender.index(
                self.model.read_contact(self.selected).informations['Gender']))
            self.update_form.submit_btn.config(command=self.edite_update_btn_command, text='Update')
        else:
            self.message.warning('warrning', 'Please select an item from list')

    def edite_update_btn_command(self):
        if all(self.update_form.get_entries_values.values()):
            if self.message.commit('Save', 'Are you save this?').conjugate():
                self.model.update_contact(self.selected, **self.update_form.get_entries_values)
                self.update_gui_table()
                self.selected = None
                self.message.info('update', 'Update Your selected item with success')
                self.update_form.destroy()
            else:
                self.update_form.destroy()
        else:
            self.message.warning('Input incorecct', 'Please fill all of the entries')
