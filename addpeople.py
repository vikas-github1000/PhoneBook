from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect("database.db")
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel. __init__(self)

        self.geometry("650x650+40+60")
        self.title("ADD PEOPLE")
        self.resizable(True, True)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#208de2')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/images.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=10, y=10)
        self.heading = Label(self.top, text='add peoples', font='magneto 20 bold', bg='white')
        self.heading.place(x=100, y=30)

        # name
        self.label_name = Label(self.bottom, text=" name    ",font= "magneto 15 bold", fg='black', bg="white")
        self.label_name.place(x=50, y=50)

        self.entry_name = Entry(self.bottom, width=25, bd=4)
        self.entry_name.insert(0, "enter Name")
        self.entry_name.place(x=250, y=50)

        # surname
        self.label_surname = Label(self.bottom, text=" surname    ", font="magneto 15 bold", fg='black', bg="white")
        self.label_surname.place(x=50, y=100)

        self.entry_surname = Entry(self.bottom, width=25, bd=4)
        self.entry_surname.insert(0, "enter Name")
        self.entry_surname.place(x=250, y=100)

        # email

        self.label_email = Label(self.bottom, text=" email    ", font="magneto 15 bold", fg='black', bg="white")
        self.label_email.place(x=50, y=150)

        self.entry_email = Entry(self.bottom, width=25, bd=4)
        self.entry_email.insert(0, "enter Name")
        self.entry_email.place(x=250, y=150)


        # phone number
        self.label_phone = Label(self.bottom, text=" phone    ", font="magneto 15 bold", fg='black', bg="white")
        self.label_phone.place(x=50, y=200)

        self.entry_phone = Entry(self.bottom, width=20, bd=4)
        self.entry_phone.insert(0, "enter phone")
        self.entry_phone.place(x=250, y=200)

        # address
        self.label_address = Label(self.bottom, text=" add    ", font="magneto 15 bold", fg='black', bg="white")
        self.label_address.place(x=50, y=250)

        self.entry_address = Entry(self.bottom, width=25, bd=4)
        self.entry_address.insert( 0,  "address")
        self.entry_address.place(x=250, y=250)

        # buttons
        button = Button(self.bottom, text="add in contact", command=self.add_people())
        button.place(x=270, y=300)

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        #address = self.entry_address.get()
        print(name)









