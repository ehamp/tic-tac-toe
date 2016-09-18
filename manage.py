from database import db
import app
from flask import Flask, request, render_template, session, url_for, Response
import json
import os
import uuid
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') if os.environ.get('DATABASE_URL') else "sqlite:////tmp/test.db"
db.init_app(app)
app.secret_key = str(uuid.uuid4())

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@app.route("/boardstate", methods=['GET'])
def board():
    return 'hello its me'


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200


@manager.command
def setup_db():
    with app.app_context():
    # print app
        db.drop_all()
        db.create_all()
        db.session.commit()
    print "database is set up!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    manager.run()