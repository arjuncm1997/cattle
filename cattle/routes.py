from flask import Flask, render_template, request, redirect,  flash, abort, url_for
from cattle import app,db,bcrypt
from cattle.models import *
from cattle.forms import *



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/playout')
def playout():
    return render_template("playout.html")

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method=='POST':
        name= request.form['name']
        email= request.form['email']
        phone= request.form['phone']
        subject= request.form['subject']
        message= request.form['message']
        print(message)
        hashed_password = bcrypt.generate_password_hash(name).decode('utf-8')
        print(hashed_password)
        new1 = Feedback(name=name,email=email,phone=phone,subject=subject,message=message,usertype='user')
        try:
            db.session.add(new1)
            db.session.commit()
            return redirect('/')

        except:
            return 'not add'  
    return render_template("contact.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/registeruser',methods=['GET','POST'])
def registeruser():
    form=RegistrationForm()
    if form.validate_on_submit():
        new = Login(username= form.username.data, email=form.email.data, password=form.password.data,phone = form.phone.data,usertype= 'user' )
        db.session.add(new)
        db.session.commit()
        flash('Your account has been created! waiting for approval', 'success')
        return redirect('/plogin')
    return render_template("registeruser.html")

@app.route('/registerseller')
def registerseller():
    return render_template("registerseller.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/uindex')
def uindex():
    return render_template("uindex.html")
@app.route('/ulayout')
def ulayout():
    return render_template("ulayout.html")

@app.route('/sindex')
def sindex():
    return render_template("sindex.html")

@app.route('/slayout')
def slayout():
    return render_template("slayout.html")

@app.route('/aindex')
def aindex():
    return render_template("aindex.html")