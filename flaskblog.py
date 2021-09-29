from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
 
@app.route("/")
@app.route("/home")
def home():
    return render_template('HomePage-1-.html')
@app.route("/detail")
def detail():
    return render_template('KR-Handloom-Sarees.html')
@app.route("/login")
def login():
    return render_template('Login-Page.html')
@app.route("/profile")
def profile():
    return render_template('Profile-Page.html')
@app.route("/home2")
def home2():
    return render_template('Home-Page-2.html')
@app.route("/scheme")
def scheme():
    return render_template('Scheme.html')
@app.route("/dashboard")
def dashboard():
    return render_template('Dash-Board.html')
@app.route("/map")
def about():
    return render_template('index.html')
@app.route("/feed")
def feed():
    return render_template('feed.html')

if __name__=='__main__':
    app.run(debug=True)