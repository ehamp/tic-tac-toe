from app import app
from flask import request, Response
import os
import slack as slack

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'


@app.route('/boardstate', methods=['GET'])
def board():
    return 'hello its me board XXX 000 XXX'


@app.route('/test', methods=['GET','POST'])
def create_game():
    slack.message_game_state()
    return "hi hi hi"