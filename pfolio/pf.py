# simple web page intended to showcase assorted personal projects

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html') 

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
