import sqlite3
import os.path

class SqliteDb:

        # constructor is used to make whole database and its tables if thd .db file is not available or deleted

        def __init__(self):
            if os.path.exists('Clinic.db') == False:   #check if .db file is available in project folder(file is not deleted or corrupted)

              conn = sqlite3.connect('Clinic.db')
              conn.execute("CREATE TABLE patient(NAME VARCHAR(50),File_number VARCHAR(50) ,   PRIMARY KEY(File_number) );")
              conn.execute(
                  "CREATE TABLE information(File_number VARCHAR(50) NOT NULL,  medicine VARCHAR(50) NOT NULL,meetingdates VARCHAR(50) NOT NULL, paid_money VARCHAR(50) NOT NULL,   FOREIGN KEY (File_number ) REFERENCES patient(File_number) ON DELETE CASCADE );")
              conn.execute("PRAGMA foreign_keys = ON;")




        #this method is for inserting data into database

        def insert_into_database(self,sql,val):

          try:
            # inserting the values into the table
            conn = sqlite3.connect('Clinic.db')
            cur = conn.cursor()
            cur.execute(sql,val)
            conn.commit()

          except sqlite3.Error as error:

              print("Failed to insert data into sqlite table", error)

          print(cur.rowcount, "record inserted!")

        # this method is for extract database records
        def show_database_records(self,sql):
          conn = sqlite3.connect('Clinic.db')
          cursor = conn.cursor()

          try:

            result=cursor.execute(sql)
            data=list(cursor.fetchall())   #convert fetched data to list for convenience of working


            return data

          except sqlite3.Error as error:

              print("Failed to read data from sqlite table", error)

        # this method is for deleting data from database
        def delete_database_records(self,sql):

          conn = sqlite3.connect('Clinic.db')
          cur = conn.cursor()
          cur.execute("PRAGMA foreign_keys = ON ;")


          try:

            cur.execute(sql)
            conn.commit()
          except:

            conn.rollback()

          conn.close()

          # this method is for updating rows of tables

          def update_database():
                conn = sqlite3.connect('Clinic.db')
                cur = conn.cursor()

                try:
                      # updating the name of the employee whose id is 110
                      cur.execute("update information set Email = '@gmial.com' where id = 19")
                      conn.commit()
                except:

                      conn.rollback()

                conn.close()
