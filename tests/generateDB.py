from flask import Flask
from OOZero import create_app
from OOZero.model import db
import OOZero.user_model as user
import OOZero.event_model as event
import datetime
import argparse

def generateDB():
    db.drop_all()
    db.create_all()

def add(entry):
    db.session.add(entry)
    db.session.commit()

def generatePopulateDB():
    generateDB()
    user.addUser(username="username", password="password", name="name", email="email@email.email")
    user.addUser(username="test", password="bad password", name="testname")
    user.addUser(username="Jeff", password="jeff", name="Jeff jeff", email="jeff@jeff.jeff")
    user.addUser(username="another User", password="worse password")
    event.createEvent(name="Wake up", owner=user.getUser("test").id, event_type=event.EventType.REMINDER, start_time=datetime.datetime.now())
    event.createEvent(name="Rocks", owner=user.getUser("Jeff").id, description="Granit, Bassalt, Quartz", event_type=event.EventType.NOTE)
    event.createEvent(name="Short party", owner=user.getUser("username").id, event_type=event.EventType.EVENT, start_time=datetime.datetime.now(), end_time=datetime.datetime.now() + datetime.timedelta(hours=3))
    event.createEvent(name="Secrets", owner=user.getUser("test").id, event_type=event.EventType.ENCRYPTED, password="sure", description="Some passwords, SSNs, creditcard numbers, and otherthings you shouldn't trust this app with")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OOZero sqlite database")
    parser.add_argument('-c', type=str, metavar='CONFIG', default="DevelopmentConfig", help="Which set of settings found under OOZero/config.py to load, determins db name and location")
    parser.add_argument('-g', type=bool, metavar='GENERATE', default=False, help='Generate dummy data for testing, defaults to False')
    args = parser.parse_args()

    app = create_app("OOZero.config." + args.c)
    with app.app_context():
        if args.g:
            generatePopulateDB()
        else:
            generateDB()