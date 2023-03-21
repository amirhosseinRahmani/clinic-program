import tkinter
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mainpack.sqlite_db import SqliteDb

db=SqliteDb()



class MyTopLevel:




    #when user enter file number to see information at first , this method give entry value as file number and ...
    def get_entry_value(self,e1,root):

        self.entryvalue = str(e1.get())   #give file number from user
        sql ="SELECT patient.Name, information.File_number,information.medicine, information.meetingdates, information.paid_money  FROM information   INNER JOIN patient  ON information.File_number = patient.File_number where patient.File_number= '%s' " %self.entryvalue
        self.sqlvalue = db.show_database_records(sql) #show all patient info from information table


        sql2= " select patient.File_number from patient where File_number = '%s' "  % self.entryvalue
        isregistered = db.show_database_records(sql2)  #show if this file number is registered in patient table


        if len(isregistered) == 0: #patient is not registered
            messagebox.showinfo("Error", "Patient Is Not Registerd")
            self.sqlvalue = [["", "", "", ""]]   #if patient is not registered so there is no informations , so set sqlvalue to list that is not empty

        if len(self.sqlvalue) == 0 and len(isregistered) != 0:  #patient is  registered but no information  recorded yet
            self.sqlvalue = [["", "", "", "" ,""]]  #patient has no record yet so set a list that is not empty so that tree can show empty row
            self.make_tree(root)   #call maketree method to make new records

        if self.entryvalue == self.sqlvalue[0][1] and len(isregistered) != 0:  #user is registered and information has record

            self.make_tree(root)



    def make_tree(self ,root):

        top = Toplevel(root, background="#292732")
        top.geometry("1000x500")

        style = ttk.Style()
        style.theme_use('clam')



        #making tree
        tree = ttk.Treeview(top, column=("Name","Filenumber","Medicine","Meetings","Paid_history"),selectmode='browse',show='headings')
        scrollbar = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)
        tree.column("# 1", anchor=CENTER, stretch=YES)
        tree.heading("# 1", text="Name")
        tree.column("# 2", anchor=CENTER, stretch=YES)
        tree.heading("# 2", text="Filenumber")
        tree.column("# 3", anchor=CENTER, stretch=YES)
        tree.heading("# 3", text="Medicine")
        tree.column("# 4", anchor=CENTER, stretch=YES)
        tree.heading("# 4", text="Meetings")
        tree.column("# 5", anchor=CENTER, stretch=YES)
        tree.heading("# 5", text="Paid_history")
        for x in self.sqlvalue:  # sqlvalue is data recorded in database for patient


             tree.insert('', 'end', text="1", values=(x[0], x[1], x[2], x[3], x[4]))  # insert all sqlvalue to tree


        tree.pack(fill='both', expand=True)

        l3 = Label(top, text="Medicine:", width=10, foreground="yellow", background='#292732')
        l3.pack(side=LEFT)
        t3 = Entry(top, foreground="yellow", background='#292732')
        t3.pack(side=LEFT)

        l4 = Label(top, text="Paid_money:", width=10, foreground="yellow", background='#292732')
        l4.pack(side=LEFT)
        t4 = Entry(top, foreground="yellow", background='#292732')
        t4.pack(side=LEFT)
        b5 = Button(top, text='Delete Record', width=15, command=lambda: self.delete_data(root ,top ,tree), foreground="yellow" ,background='#292732')
        b5.pack(side=RIGHT)
        b2 = Button(top, text='Add Record', width=15, command=lambda: self.add_data(tree, t3, t4), foreground="yellow"
                    ,background='#292732')
        b2.pack(side=RIGHT)

        top.mainloop()


    def add_data(self,tree ,t3 ,t4):
        entryvalue=self.entryvalue     #entry value is file number give from user


        sql ="select patient.Name from patient where File_number = '%s' " %entryvalue   #give patient name from patient table
        name= db.show_database_records(sql)
        medicine = t3.get()
        paid_money = t4.get()
        date = datetime.datetime.now()

        sql2 = "insert into information (File_number,medicine,meetingdates,paid_money) values (?, ?, ?, ?) "
        val = (entryvalue, medicine, date, paid_money)

        db.insert_into_database(sql2,val)
        tree.insert('', 'end', text="1", values=(name, entryvalue, medicine, date, paid_money))   #add new data to tree using add record button

    def delete_data(self,root,top,tree):
        # Get selected item to Delete
        selected_item = tree.selection()[0]   #when user click on a row the item will be selected

        current_item = tree.focus()     #focus give selected row information
        item= tree.item(current_item)   # item function give the item values to be used for delete operation in database



        name= item["values"][0]
        filenumber= item["values"][1]
        medicine= item["values"][2]
        date= item["values"][3]
        paid_money= item["values"][4]

        tree.delete(selected_item)
        sql= "delete from information where File_number='%s' "%filenumber+ "  and medicine='%s' "%medicine+ "and meetingdates='%s'"%date+ " and paid_money='%s' "%paid_money+ " "
        db.delete_database_records(sql)



