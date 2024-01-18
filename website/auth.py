from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category="success")
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category="error")
        else:
            flash('Email does not exist.', category="error")

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('email already exists', category="error")
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
            login_user(newUser, remember=True)
            flash('success', category="success")
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)
