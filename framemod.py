from tkinter import *

class framemod(Frame):
    def __init__(self, container,id,  *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.id = id
        