#-*- coding: utf-8 -*-

#Ping Modul import
import importlib.util
lorem=importlib.util.spec_from_file_location("ping","scripte/ping.py")
ping = importlib.util.module_from_spec(lorem)
lorem.loader.exec_module(ping)

#Flask imports
from flask import Flask, render_template, url_for, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

#Form imports
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

#Initialisierung - Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['TESTING'] = True

#Initialisierung - SQLAlchemy - Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Datenbanken und lokale Sessions synchronisieren
migrate = Migrate(app, db)

#Flask - Login Manager initialisieren
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Hooks
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Modelle
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],render_kw={"placeholder":"Username"})
    password = StringField(validators=[InputRequired(), Length(min=4, max=20)],render_kw={"placeholder":"Password"})
    submit = SubmitField("Register")
    def validate_username(self,username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("Username bereits vergeben.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],render_kw={"placeholder":"Username"})
    password = StringField(validators=[InputRequired(), Length(min=4, max=20)],render_kw={"placeholder":"Password"})
    submit = SubmitField("Login")

#Backend routen
#Index
@app.route('/')
def home() -> None:
    return render_template('index.htm', title='Startseite')

#Registrierung
@app.route('/register',methods=['POST','GET'])
def register() -> None:
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e :
            print(e)
        return redirect(url_for('login'))

    return render_template('register.htm', title='Register', form = form)

#Login
@app.route('/login',methods=['GET', 'POST'])
def login() -> None:
    form = LoginForm()
    user = User.query.filter_by(username=form.username.data).first()
    try:
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                session['username'] = str(form.username.data)
                login_user(user)
                return redirect(url_for('dashboard'))
    except Exception as e:
        print(e)
    return render_template('login.htm', title='Login', form = form)

#Logout
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#Hilfe
@app.route('/help')
def help() -> None:
    return render_template('help.htm', title='EasterEgg:)')

#Logs
@app.route('/logs')
def logs() -> None:
    return render_template('logs.htm', title='Logs')

#Profil
@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil():
    user_id = session["username"]
    return render_template('profil.htm', title = 'Profil', user = user_id)

#Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    user_id = session["username"]
    #Für den User eine neue Instanz der Commandoklasse initieren
    try:
        ret_env = ping.execute_CMD()
        scripte = ret_env.show_executable()
        #scripte = ["Ping","Tracert"]
    except Exception as e:
        print(e)

    if request.method == "POST":
        if request.form['ping.py']:
            return redirect(str(url_for('show_res',command="ping",adress="www.noname-records.de")))
    
    return render_template('dashboard.htm', title = 'Dashboard', user = user_id, out = scripte)

#Ergebnissanzeige
@app.route('/show_res/<command>/<adress>',methods=['GET','POST'])
@login_required
def show_res(command,adress):
    user_id = session["username"]
    result = ping.execute_CMD().runtime()
    if(result==None):
        result = "ERROR GETTING DATA"
    return render_template('result.htm', title = 'Ergebnis', res = result, user = user_id)

if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():
    db.create_all()