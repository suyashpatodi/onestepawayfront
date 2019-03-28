from flask import Flask, render_template, request

#Imported for database
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/onestepawaydb'

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    #(name, email, password, contact , service , address )
    name=db.Column(db.String(80), primary_key=True)
    emailid=db.Column(db.String(80),nullable=True)
    password=db.Column(db.String(120),nullable=True)
    contact=db.Column(db.String(80),nullable=True)
    service=db.Column(db.String(80),nullable=True)
    address=db.Column(db.String(80),nullable=True)

class Service(db.Model):
    __tablename__='service'
    #(name, email, password, contact , service , address )
    oname=db.Column(db.Integer, primary_key=True)
    bname=db.Column(db.String(80),nullable=True )
    oemailid=db.Column(db.String(80),nullable=True)
    opassword=db.Column(db.String(120),nullable=True)
    ocontact=db.Column(db.String(80),nullable=True)
    oservice=db.Column(db.String(80),nullable=True)
    oaddress=db.Column(db.String(80),nullable=True)
    odescribe=db.Column(db.String(80),nullable=True)
    olongitude=db.Column(db.Integer,nullable=True)
    olatitude=db.Column(db.Integer,nullable=True)
    imagename=db.Column(db.String(120),nullable=True)
    oimage=db.Column(db.LargeBinary,nullable=True)


@app.route("/login")
def login():
    return(render_template("login.html"))

@app.route("/register")
def register():
    return render_template("Registration.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registeru",methods=['GET','POST'])
def registeru():
    if request.method=='POST':
        name=request.form.get('name', False)
        email=request.form.get('email', False)
        password=request.form.get('pass', False)
        contact=request.form.get('phone', False)
        service=request.form.get('service', False)
        address=request.form.get('address', False)
        entry=User(name=name, contact=contact, emailid=email,password=password, service=service, address=address )
        db.session.add(entry)
        db.session.commit()
        return render_template('login.html')
    return render_template('Registrationu.html')    

@app.route("/registerb",methods=['GET','POST'])
def registerb():
    if request.method=='POST':
        oname=request.form.get('oname', False)
        bname=request.form.get('bname', False)
        oemailid=request.form.get('oemailid', False)
        opassword=request.form.get('opassword', False)
        ocontact=request.form.get('ocontact', False)
        oservice=request.form.get('oservice', False)
        oaddress=request.form.get('oaddress', False)
        odescribe=request.form.get('odescribe', False)
        olatitude=request.form.get('olatitude', False)
        olongitude=request.form.get('olongitude', False)
        # file1=request.files['file1']
        #  ,imagename=file1.filename , oimage=file1.read()


        entry2=Service(oname=oname, bname=bname,opassword=opassword, ocontact=ocontact, oemailid=oemailid, oservice=oservice, oaddress=oaddress ,odescribe=odescribe, olatitude=olatitude, olongitude=olongitude)
        db.session.add(entry2)
        db.session.commit()
        return render_template('login.html')
    return render_template("Registrationb.html")

if __name__ == "__main__":
    app.run(debug=True)