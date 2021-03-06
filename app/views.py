from . import app
from flask import request, Response
from game import Game
import slackclient as slack
from database import db

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'


@app.route('/boardstate', methods=['GET'])
def board():
    return 'hello its me board XXX 000 XXX'


@app.route('/ttt', methods=['GET','POST'])
def check_game_state():
    g = Game('p1', 'p2')
    db.session.add(g)
    db.session.commit()
    g = Game.query.all().first()
    if g is None or g.is_game_over:
        return "ho ho ho"
    else:
        slack.message_game_state()
    return "hi hi hi"