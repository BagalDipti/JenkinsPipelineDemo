import sqlite3 as sq
con=sq.connect("../Jenkins_Demo/Student.db")
cur=con.cursor()
cur.execute("create table student(id INTEGER PRIMARY KEY AUTOINCREMENT,fname text,lname text,email text,password text)")
con.commit()
con.close()