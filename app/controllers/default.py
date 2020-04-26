from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print()
    else:
        print()

    return render_template('login.html', form=form)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/<user>')
#@app.route('/', defaults={"user":None})
#def profile(user):
#    return render_template('base.html', user=user)
