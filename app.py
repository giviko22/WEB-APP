from flask import *
import sqlite3
from datetime import date

app = Flask(__name__) 

@app.route("/")  
def index():  
 return render_template("index.html")

@app.route("/edit")  
def edit():   
 return render_template("edit.html")

@app.route("/editing",methods = ["POST"])  
def editing():
 id = request.form["id"]   
 with sqlite3.connect("database.db") as con:  
  try:  
   a = request.form["a"]  
   b = request.form["b"]  
   c = request.form["c"] 
   d = date.today()
   e = request.form["e"] 
   cur = con.cursor()   
   cur.execute("UPDATE news SET a=?, b=?, c=?, d=?, e=? WHERE id=?", (a,b,c,d,e,id))  
   con.commit()  
   msg = "ინფორმაცია შეიცვალა !"   
  except:    
   msg = "სამწუხაროდ ინფორმაცია არ შეიცვალა"  
  finally:  
   return render_template("editsuccess.html",msgs = msg) 


@app.route("/add")  
def add():   
 return render_template("add.html")

@app.route("/savedetails",methods = ["POST"])  
def saveDetails():    
 with sqlite3.connect("database.db") as con:
  try:  
   a = request.form["a"]  
   b = request.form["b"]  
   c = request.form["c"] 
   d = date.today()
   e = request.form["e"]  
   cur = con.cursor()   
   cur.execute("INSERT into news (a, b, c, d, e) values (?,?,?,?,?)",(a,b,c,d,e))  
   con.commit()  
   msg = "სიახლე შეტანილია !"   
  except:   
   msg = "სამწუხაროდ სიახლე არ დაემატა"  
  finally:  
   return render_template("success.html",msgs = msg)  

@app.route("/view")  
def view():  
 con = sqlite3.connect("database.db")  
 con.row_factory = sqlite3.Row  
 cur = con.cursor()  
 cur.execute("select * from news")   
 rows = cur.fetchall()  
 return render_template("view.html",rows = rows)  


@app.route("/onlyone")  
def onlyone():   
 return render_template("onlyone.html")

@app.route("/viewone",methods = ["POST"])  
def viewone():   
 id = request.form["id"]
 row = 0
 with sqlite3.connect("database.db") as con:
   try:    
    cur = con.cursor()  
    cur.execute("SELECT * from news WHERE id = ?", (id))   
    row = cur.fetchone()
    con.commit()
    msg = "სიახლე"
   except:
    msg = "გთხოვთ მიუთითოთ ნომერი"
   finally:      
    return render_template("viewone.html",msgs = msg, row = row) 



@app.route("/delete")  
def delete():  
 return render_template("delete.html")  

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():  
 id = request.form["id"]  
 with sqlite3.connect("database.db") as con:  
  try:  
   cur = con.cursor()  
   cur.execute("delete from news where id = ?",id)  
   msg = "სიახლე წაშლილია !"   
  except:  
   msg = "სიახლე არ წაიშალა"  
  finally:  
   return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":  
 app.run(debug = True)  