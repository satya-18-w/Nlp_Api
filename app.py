from flask import Flask,render_template,request
from db import Database

app = Flask(__name__)
dbo=Database()

@app.route('/')
def index():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/perform_registration' , methods=["post"])
def perform_registration():
    name=request.form.get("User_Name")
    email=request.form.get("User_Email")
    password=request.form.get("User_password")
    
    response=dbo.insert(name,email,password)
    if response:
        return render_template("login.html" , message="Registration Sucessful.  Kindly Login to proceed")
    else:
        return render_template("register.html" , message="Email Already Exist")
        
    
    
@app.route("/perform_login",methods=["post"])
def perform_login():
    
    email=request.form.get("User_Email")
    password=request.form.get("User_Password")
    response=dbo.search(email,password)
    if response:
        return "Login Sucessfull"
    else:
        return render_template("login.html",message="Invalid Password")
    
    
app.run(port=5000,debug=True)



