from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'thisisjustasupersecretrandomkey123'

posts = [
    {
        'author': 'Pop Minho',
        'title': 'Run NodeJs on your ass',
        'content': 'Now you can run Nodejs in your ass, both ways',
        'date_posted':'April 21,2021'
    }, {
        'author': 'Florin Pop',
        'title': 'Learn JS in 3 mins',
        'content': 'The intriguing way to learn new thigis',
        'date_posted':'May 2,2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="About Page")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)
    
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title="Login",form=form)

if __name__ == "__main__":
    app.run(debug=True) 