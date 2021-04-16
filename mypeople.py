from tkinter import *
from addpeople import AddPeople
import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel. __init__(self)

        self.geometry("650x650+60+40")
        self.title("MY PEOPLE")
        self.resizable(True, True)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#208de2')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/images.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=10, y=10)

        self.heading = Label(self.top, text='my peoples', font='magneto 20 bold', bg='white')
        self.heading.place(x=100, y=30)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0, column=0, padx=(40, 0))
        self.scroll.config(command=self.listBox.yview)

        self.scroll.config(command=self.listBox.yview)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        btnadd = Button(self.bottom, text="Add",width=12,font='magneto 12 bold', command=self.add_people)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnupdate = Button(self.bottom, text="Update", width=12, font='magneto 12 bold')
        btnupdate.grid(row=0, column=2, padx=20, pady=60, sticky=N)

        btnDisplay = Button(self.bottom, text="Display", width=12, font='magneto 12 bold')
        btnDisplay.grid(row=0, column=2, padx=20, pady=110, sticky=N)

        btndelet = Button(self.bottom, text="Delete", width=12, font='magneto 12 bold')
        btndelet.grid(row=0, column=2, padx=20, pady=160, sticky=N)


    def add_people(self):
        add_page = AddPeople()




