
from datetime import datetime
from flask import Flask, render_template, session, request, \
    url_for, redirect, Response, jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("settings")
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))


@app.route('/')
def index():
    return render_template("index.html")


# ---
