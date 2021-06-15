from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True
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

if __name__ == "__main__":
    app.run(debug=True) 