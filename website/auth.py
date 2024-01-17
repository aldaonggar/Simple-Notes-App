from flask import Blueprint, render_template, request, flash

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
        password1 = request.form.get('password1')
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
            flash('error', category="success")    #TODO add user to db    
    
    return render_template("sign_up.html")
