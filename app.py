import datetime,os,smtplib,ssl
from flask import Flask,render_template,request,session
from flask_session import Session
#from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key = 'any random string'


#configure session
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
#Session(app)

#configure smtp

#configure db
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'alex9122'
#app.config['MYSQL_DB'] = 'web_database'

#mysql=MySQL(app)


@app.route("/sendmail",methods=["POST"])
def sendmail():
    if request.method=="POST":
        port=465
        smtp_server="smtp.gmail.com"
        receiver_email="alexgathua3@gmail.com"
        password="testpy301"
        name=request.form.get("name").upper()
        sender_email=request.form.get("email")
        subject=request.form.get("subject").upper()
        message=request.form.get("message")
        
        return  render_template("python1.html",name=name,email=email)


@app.route("/<string:name>")
def any(name): 
    name=name.upper()
    headline="HELLO MY GOOD PEOPLE"
    return render_template("python.html",headline=headline)



@app.route('/bye')
def bye():
    #name=name.upper()
   # now=datetime.datetime.now()

    #headline=now.month==1 and now.day==1#boolean expression
    #names=["alex","james","mark"]
    return render_template("index.html")

#notes=[]
@app.route("/more",methods=["GET","POST"])
def more():
   if request.method=="POST":
      name=request.form.get("name").upper()
      email=request.form.get("email")
     #cur=mysql.connection.cursor()
     #if cur.execute("SELECT * FROM logon_data WHERE username= "+ name +", email="+email+""):
        #return render_template("python1.html",name=name,email=email)
       # cur.close()
     #mysql.connection.commit()
      return render_template("python1.html",name=name,email=email)


    
@app.route("/page",methods=["POST"])
def page():
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method=="POST":
        note=request.form.get("note").capitalize()
        session["notes"].append(note)
        return render_template("python1.html",notes= session["notes"])

if __name__=="__main__":
  # app.debug= True
   app.run(debug=True)