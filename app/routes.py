from flask import render_template, redirect, url_for, session, jsonify
from app import app, db
from app.forms import LoginForm, RegisterForm, RezeptForm
from app.models import User, Recipe 
from hashlib import sha256


@app.route('/')
@app.route('/index')
def index():
    if "benutzer" in session:
        recipe = Recipe.query.all()
        return render_template('index.html', recipe = recipe)
    else:
        return redirect(url_for('login'))


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user =  User.query.filter_by(username=form.username.data).first()
        if user is None:
            user= User(username=form.username.data, email=form.email.data, password_hash=sha256(form.password.data.encode('utf-8')).hexdigest()) 
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return redirect(url_for('register'))
         
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password_hash=sha256(form.password.data.encode('utf-8')).hexdigest()).first()
        if user is None:
            return redirect(url_for('login'))   
        else:
            session["benutzer"] =  user.id
            return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/recipe', methods=['GET','POST'])
def recipe():
    form = RezeptForm()

    if "benutzer" in session:
        if form.validate_on_submit():
            recipe = Recipe(recipename=form.rezeptname.data, ingredients=form.zutaten.data, cookingistructions=form.kochanleitung.data, user_id=session["benutzer"])
            db.session.add(recipe)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('recipe.html', form=form)
    else:
        return redirect(url_for('login'))
    

    

@app.route('/logout')
def logout():
    if "benutzer" in session:
        session.pop ("benutzer", None)
        return redirect(url_for('login'))




@app.route('/api/alle_rezepte')
def api_allerezepte():
    recipe = Recipe.query.all()
    return jsonify([s.toDict() for s in recipe])

@app.route('/api/alle_benutzer')
def api_allebenutzer():
    user = User.query.all()
    return jsonify([s.toDict() for s in user])