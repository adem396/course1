from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import registrationForm, loginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '568454164zeffkygfve84frez'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('post', backref='author', lazy=True)

    def __repr__(self):
        return f"user('{self.username}','{self.email}','{self.image_file}')"
    
class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"post('{self.title}','{self.date_posted}')"
    
post = [
    {
        'author': 'hamer jephry',
        'title': 'the last',
        'content': 'first post content',
        'date_posted': 'april 20,2018'
    },
    {
        'author': 'cristiano',
        'title': 'the best',
        'content': 'second post content',
        'date_posted': 'november 16,2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def regestration():
    form = registrationForm()
    return render_template("regester.html", title='regester', form=form)


@app.route("/login")
def login():
    form = loginForm()
    return render_template("login.html", title='login', form=form)


if __name__ == "__main__":
    app.run()
