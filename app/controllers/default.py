from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login_manager

from app.models.tables import User
from app.models.forms import LoginForm

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

# Login route
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
#        umail = User.query.filter_by(email=form.email.data).first()
        
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for('index'))

#        elif umail and umail.password == form.password.data:
#            login_user(umail)
#            flash("Logged in.")
#            return redirect(url_for('index'))

        else:
            flash("Nome de usuário ou senha inválidos.")

    return render_template('login.html', form=form)

# Logout route
@app.route('/logout')
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for('index'))

# Index/home route
@app.route('/')
def index():
    return render_template('index.html')

# Profile route
#@app.route('/<user>')
#@app.route('/', defaults={"user":None})
#def profile(user):
#    return render_template('base.html', user=user)

# Test of insertion and query database
#@app.route('/teste/<info>')
#@app.route('/teste', defaults={'info': None})
#def teste(info):
#    r = User('Ayrton Leandro', 'ayrton.leandro', 'ayrton.leandro@gmail.com', 'meninodeprograma')
#    db.session.add(r)
#    db.session.commit()
#    print(r.username, r.name, r.email, r.password)
#    return 'ok'
