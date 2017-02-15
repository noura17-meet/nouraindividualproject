from flask import Flask, render_template,request, redirect, url_for
from database import *
from flask import session as login_session
from flask import g

app = Flask(__name__)
app.secret_key= "something"

engine = create_engine ('sqlite:///forum.db')
Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine, autoflush = False)
session = DBsession()
@app.route('/')
@app.route('/signup', methods = ['GET','POST'])
def sign_up():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        if name == None or email == None or password == None:
            flash("Your form is missing arguments")
            return redirect(url_for('sign_up'))
            if session.query(User).filter_by(email = email).first() is not None:
                flash("A user with this email address already exists")
                return redirect(url_for('sign_up'))
                customer = Customer(name = name, email=email)
                customer.hash_password(password)
                session.add(user)
                session.commit()
                flash("User Created Successfully!")
                return redirect(url_for('mainpage.html'))
    else:
                return render_template('signin.html')

@app.route('/signin', methods = ['GET','POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email is None or password is None:
            flash('Missing Arguments')
            return redirect(url_for('signin'))
        if  verify_password  (email , password):
            user = session.query(User).filter_by(email=email).one()
            flash('Welcome, %s'% user.name)
            signin_session['name'] = user.name
            signin_session['email'] = user.email
            signin_session['id'] = user.id
            return redirect(url_for('mainpage'))
    else:
            flash('incorrect username/password')
            return redirect(url_for(signin))

@app.route('/book', methods= ['GET', 'POST'])
def book():
    if request.method == 'GET':
        return render_template("book1.html")

if __name__== '__main__':
    app.run(debug=True)
        


