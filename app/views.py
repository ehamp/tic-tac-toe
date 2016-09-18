from app import app
from flask import request, Response
import os

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'


@app.route("/boardstate", methods=['GET'])
def board():
    return 'hello its me board XXX 000 XXX'


@app.route('/slack', methods=['POST'])
def inbound():
    SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200