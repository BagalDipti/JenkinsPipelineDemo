from flask import *
import sqlite3 as sq

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("Registration1.html");

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        firstname=request.form["fname"]
        lastname = request.form["lname"]
        email = request.form["email"]
        password= request.form["password"]

        con=sq.connect("Student.db")
        cur=con.cursor()
        cur.execute("insert into student(fname,lname,email,password)values(?,?,?,?)",(firstname,lastname,email,password))
        con.commit()
        con.close()
        return redirect(url_for("display"))
    else:
        return redirect(url_for("home"))

@app.route("/display")
def display():
    con=sq.connect("Student.db")
    cur=con.cursor()
    cur.execute("select * from student")
    data=cur.fetchall()


    return render_template("display.html",displaydata=data)

#delete
@app.route('/delete/<int:id>')
def del_action(id):
    con = sq.connect("Student.db")
    cur = con.cursor()
    cur.execute("delete from student where id=?",[id])
    con.commit()
    con.close()
    return redirect(url_for("display"))

@app.route('/edit/<int:id>')
def edit_action(id):
    con = sq.connect("Student.db")
    cur = con.cursor()
    cur.execute("select * from student where id=?",[id])
    data=cur.fetchone()
    return render_template("Edit.html",edit_data=data)

#update
@app.route("/update",methods=["POST","GET"])
def update():
    if request.method=="POST":
        id=request.form["id"]
        firstname=request.form["fname"]
        lastname = request.form["lname"]
        email = request.form["email"]
        password= request.form["password"]

        con=sq.connect("Student.db")
        cur=con.cursor()
        cur.execute("update student set fname=?, lname=?,email=?,password=? where id=?",(firstname,lastname,email,password,id))
        con.commit()
        con.close()
        return redirect(url_for("display"))
    else:
        return redirect(url_for("display"))




if __name__=='__main__':
    app.run(debug=True)