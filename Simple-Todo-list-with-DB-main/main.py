from asyncio import tasks
from email.policy import default
from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import enum
import os

app= Flask(__name__)
app.secret_key="super secret key"

db_path=os.path.join(os.path.dirname(__file__), 'app.db')

app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{db_path}'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    tasks=db.relationship("Task",backref="user",lazy=True)

class TaskStatus(enum.Enum):
    COMPLETED="Completed"
    CLOSED="Closed"
    OPEND="Opend"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200),nullable=False)
    status = db.Column(db.Enum(TaskStatus),default=TaskStatus.OPEND)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

db.create_all()    


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/task")
def task():
    logged_user =session["user_id"]
    task_list= Task.query.filter_by(user_id=logged_user)
    return render_template("task.html",username=logged_user,tasks=task_list)    

@app.route("/logout", methods=["POST","GET"])
def logout():
    if request.method == "POST":
        session["user_id"]=None
        return redirect("/") 

  

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username=request.form["username"]
        
        existing_user=User.query.filter_by(username=username).first()
        
        if existing_user is None:
          user=User(username=username)
          db.session.add(user)
          db.session.commit()
          existing_user=user
        
        session["user_id"]=existing_user.id
        return redirect("/task") 

    return render_template("login.html")    

if __name__=="__main__":
    app.run()     