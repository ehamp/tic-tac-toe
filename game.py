from database import db

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    game_over = db.Column(db.Boolean, default=False)
    player1 = db.Column(db.String(64))
    player2 = db.Column(db.String(64))
    turn = db.Column(db.String(64))

    def __init__(self, player1, player2):
        if self.player1 is None:
            self.player1 = player1
        if self.player2 is None:
            self.player2 = player2
        if self.turn is None:
            self.turn = player1

    def is_game_over(self):
        return self.game_over

    def whose_turn(self):
        return self.turn

    def update_whose_turn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def game_is_over(self):
        self.game_over=True







