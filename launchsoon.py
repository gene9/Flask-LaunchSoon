
from datetime import datetime
from flask import Flask, render_template, session, request, \
    url_for, redirect, Response, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import TextField, validators, PasswordField, TextAreaField

app = Flask(__name__)
app.config.from_object("settings")
db = SQLAlchemy(app)


class SignupForm(Form):
    email = TextField("Email",
             [validators.Required("Please enter your email address."),
              validators.Email("Please enter your email address.")])

    def validate(self):
        if not Form.validate(self):
            return False

        contact = Contact.query.filter_by(email=self.email.data.lower()).first()
        if contact:
            self.email.errors.append("Already signed in.")
            return False
        return True


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))


@app.route('/', methods=["GET", "POST"])
def index():
    form = SignupForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        contact = Contact()
        contact.email = form.email.data

        db.session.add(contact)
        db.session.commit()

        return render_template("subscribed.html")
    else:
        return render_template("index.html", form=form)
        
# ---
