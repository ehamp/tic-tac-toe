from app import app
from flask import request, Response
import os

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'


@app.route('/boardstate', methods=['GET'])
def board():
    return 'hello its me board XXX 000 XXX'


@app.route('/test', methods=['POST'])
def inbound():
    return "hi hi hi"