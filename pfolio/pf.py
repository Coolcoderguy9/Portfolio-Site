# simple web page intended to showcase assorted personal projects

from flask import Flask, render_template, url_for, request, flash, redirect
import sqlite3

connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()
cursor.execute("Create Table Connections (Name TEXT, Contact TEXT, Message TEXT)")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b1aa2872746a72528e6b7db9238b91922f8fd861f26d21cd'

@app.route("/")
def home():
    return render_template('main.html') 

@app.route("/contact", methods=('GET', 'POST'))
def contact():
    fields = [{'Name': 'Please enter your name', 'Contact': 'Please supply your contact information', 'Message': 'Please provide a brief message regarding your visit'}]
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        message = request.form['message']

        if not name:
            flash("Please supply a name!")
        elif not contact:
            flash("Please supply contact info!")
        elif not message:
            flash("Please leave a short message!")
        else:
            cursor.execute("INSERT INTO Connections VALUES ('name', 'contact', 'message')")
    return render_template('contact.html', fields = fields)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
