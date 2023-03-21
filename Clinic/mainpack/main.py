import tkinter
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mainpack.sqlite_db import SqliteDb
from mainpack.top_level import MyTopLevel


#instantiating database
db=SqliteDb()


class Main:

        def __init__(self):     #constructor make root and toplevel objects and all widgets of main window of program
            self.root = Tk()
            self.root.title("Clinic")
            self.root.geometry("1000x1000")
            self.root.configure(border=5, relief="ridge")
            self.mytoplevel = MyTopLevel()


            self.bg = PhotoImage(file="bg2.PNG")
            self.img_label = Label(self.root, image=self.bg)
            self.img_label.pack(side=LEFT, fill='both', expand=True)
            self.frame = Frame(self.root, width=400, height=500, relief='raised', borderwidth=5, background='#292732')
            self.frame.place(relx=.409, rely=.5, anchor=CENTER)
            self.frame.pack_propagate(0)

            self.labelframe1 = LabelFrame(self.frame, text="Patient Informations", background='#292732', foreground='yellow',height=100)
            self.labelframe1.pack(fill="both", expand=False, side=TOP)
            self.labelframe1.pack_propagate(0)

            '''frame2'''
            self.frame2 = Frame(self.frame, width=400, height=40, relief='raised', borderwidth=5, background='#292732')
            self.frame2.pack(side=TOP, fill='x', expand=False)
            self.frame2.pack_propagate(0)
            self.filenumber = Label(self.frame2, text="Filenumber:", foreground='yellow', background='#292732')
            self.filenumber.pack(side=LEFT)
            self.e1 = tkinter.Entry(self.frame2, foreground='yellow', background='#292732', relief='ridge')
            self.e1.focus()
            self.e1.pack(side=LEFT, fill='both', expand=True)
            self.b1 = Button(self.frame2, text="Check Information", command=lambda: self.mytoplevel.get_entry_value(self.e1, self.root),
                        foreground='yellow', background='#292732')
            self.b1.pack(side=RIGHT)
            '''frame2'''

            '''frame3 for user registration'''
            self.frame3 = Frame(self.frame, width=400, height=150, relief='raised', borderwidth=5, background='#292732')
            self.frame3.pack(side=TOP, fill='x', expand=False, pady=20)
            self.frame3.pack_propagate(0)
            self.labelframe2 = LabelFrame(self.frame3, text="Register Patient", background='#292732', foreground='yellow')
            self.labelframe2.pack(fill="both", expand=True, side=TOP)
            self.labelframe2.pack_propagate(0)
            self.registered_filenumber = Label(self.frame3, text="Filenumber", foreground='yellow', background='#292732')
            self.registered_filenumber.pack(side=LEFT)
            self.e2 = tkinter.Entry(self.frame3, foreground='yellow', background='#292732', width=15)
            self.e2.pack(side=LEFT)
            self.regName = Label(self.frame3, text="Name", foreground='yellow', background='#292732')
            self.regName.pack(side=LEFT)
            self.e3 = tkinter.Entry(self.frame3, foreground='yellow', background='#292732', width=15)
            self.e3.pack(side=LEFT)
            self.b2 = Button(self.frame3, text="Register", command=lambda: self.register_patient(), foreground='yellow',
                        background='#292732', width=15)
            self.b2.pack(side=RIGHT)
            '''frame3'''

            '''frame 4 for user deletion'''
            self.frame4 = Frame(self.frame, width=400, height=150, relief='raised', borderwidth=5, background='#292732')
            self.frame4.pack(side=TOP, fill='x', expand=False)
            self.frame4.pack_propagate(0)
            self.labelframe3 = LabelFrame(self.frame4, text="Delete Patient", background='#292732', foreground='yellow')
            self.labelframe3.pack(fill="both", expand=True, side=TOP)
            self.labelframe3.pack_propagate(0)

            self.deleted_filenumber = Label(self.frame4, text="Filenumber", foreground='yellow', background='#292732')
            self.deleted_filenumber.pack(side=LEFT)
            self.e4 = tkinter.Entry(self.frame4, foreground='yellow', background='#292732')
            self.e4.pack(side=LEFT)
            self.b3 = Button(self.frame4, text="Delete", command=lambda: self.delete_patient(), foreground='yellow',
                        background='#292732', width=15)
            self.b3.pack(side=RIGHT)
            '''frame 4 for user deletion'''

            self.root.mainloop()
            '''root widgets'''

        def register_patient(self):  #if patient is not registered this method give file number and name to register to database



                registeredfilenumber = self.e2.get()
                registerd_name = self.e3.get()
                if len(registerd_name) == 0:  #this is for forcing user not to leave name field empty
                    messagebox.showwarning("Error", "Name Field Should Not Be Empty")
                elif len(registeredfilenumber) == 0: #this is for forcing user not to leave file number field empty
                    messagebox.showwarning("Error", "Filenumber Field Should Not Be Empty")
                else:
                    sql = "insert into patient (Name,File_number) values (?, ?) "
                    val = (registerd_name, registeredfilenumber)
                    db.insert_into_database(sql, val)  # register patient into patient table
                    messagebox.showinfo("Done", "Patient Registered Succussfully")

        def delete_patient(self):  #delete patient compeletly

                filenumber = self.e4.get()
                if len(filenumber) == 0:  # force user not to leave file number empty
                    messagebox.warning("Error", "File Number Should Not Be Empty")

                else:
                    sql = "delete from patient where File_number = '%s'" % filenumber
                    sql2 = "select patient.File_number from patient where File_number = '%s' " % filenumber
                    patient_existance = db.show_database_records(sql2)  #check if patient filenumber is patient table

                    if len(patient_existance) == 0:  #if patient is not registered or has been deleted
                        messagebox.showerror("Error", "No Patient Available")
                    else:
                        db.delete_database_records(sql)
                        messagebox.showinfo("Done", "Patient Deleted Succussfully")



Main()  #instantiating the Main class












