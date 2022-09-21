# simple web page intended to showcase assorted personal projects

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html') 

@app.route("/contact", methods=('GET', 'POST'))
def contact():
    fields = [{'Name': 'Please enter your name', 'Contact': 'Please supply your contact information', 'Message': 'Please provide a brief message regarding your visit'}]
    return render_template('contact.html', fields = fields)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
