from flask import Flask, render_template
from forms import registrationForm, loginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '568454164zeffkygfve84frez'
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
