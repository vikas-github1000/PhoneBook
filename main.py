from tkinter import *
import datetime
from addpeople import AddPeople
from mypeople import MyPeople


date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self, master):
        self.master = master
        # frame
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#0766b5')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/phone-book.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=10, y=10)

        self.heading = Label(self.top, text='my phone book app', font='magneto 20 bold', bg='white')
        self.heading.place(x=100, y=30)

        self.date_label = Label(self.top, text="Today's date : " + date, font='arial 12 bold', fg='black', bg='white')
        self.date_label.place(x=400, y=35)

        # button1 view people
        self.viewButton = Button(self.bottom, text="View People", font='magneto 12 bold', command=self.my_people)
        self.viewButton.place(x=250, y=70)

        # button2 add people
        self.addButton = Button(self.bottom, text=" Add People", font='magneto 12 bold',command=self.add_people)
        self.addButton.place(x=250, y=130)

        # button3 about us
        self.viewButton = Button(self.bottom, text="   About Us  ", font='magneto 12 bold')
        self.viewButton.place(x=250, y=190)

    def my_people(self):
        people = MyPeople()

    def add_people(self):
        add_page = AddPeople()


def main():
    root = Tk()
    app = Application(root)
    root.title("PHONE BOOK APP")
    root.geometry("600x600+20+20")
    root.resizable(True, True)
    root.mainloop()


if __name__ == '__main__':
    main()
