from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1') #TODO hash password
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('email must be greater then 4', category="error")
        elif len(firstName) < 2:
            flash('error', category="error")
        elif password1 != password2:
            flash('error', category="error")
        elif len(password1) < 7:
            flash('error', category="error")
        else:
            newUser = User(email = email, firstName = firstName, password=generate_password_hash(password1, method='scrypt'))
            db.session.add(newUser)
            db.session.commit()
            flash('success', category="success")
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html")
