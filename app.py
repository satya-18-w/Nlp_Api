from flask import Flask,render_template,request,redirect,session
from db import Database
import api
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
        return redirect("/profile")
    else:
        return render_template("login.html",message="Invalid Password")
    
@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/ner")
def ner():
    if session:
        return render_template("ner.html")
    else:
        return redirect("/")
 
@app.route("/perform_ner",methods=["post"])
def perform_ner():
    text=request.form.get("ner_text")
    responce=api.ner(text)
    print(responce)
    result=""
    for i in responce:
        result=result + i["name"] + " " + i["category"] + "\n"
    return render_template("ner.html" ,result=result)
    
    
if __name__ == "__main__":
    
    app.run(port=5000,debug=True)



