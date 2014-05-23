#!/usr/bin/env python

from flask.ext.script import Manager
from launchsoon import app, db


manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    print "initdb is done"


@manager.command
def dropdb():
    db.drop_all()
    print "dropdb is done"


if __name__ == '__main__':
    manager.run()

# ---
