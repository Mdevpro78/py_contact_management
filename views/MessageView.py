from tkinter import messagebox


class Message:
    def __init__(self):
        self.message = messagebox

    def error(self, title, message):
        return self.message.showerror(f'{title}', f'{message}')

    def warning(self, title, message):
        return self.message.showwarning(f'{title}', f'{message}')

    def info(self, title, message):
        return self.message.showinfo(f'{title}', f'{message}')

    def commit(self, title, message):
        return self.message.askyesno(f'{title}', f'{message}')
