class Player(object):
    # modify class player in order every timel: _level up by one will 
    # increase score by 1000.
    # 1 -> 0
    # 2 -> 1000
    # 3 -> 2000
    # 4 -> 3000


    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0


    def _set_score(self, _score):
        _score = _level + 1000
            

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can not be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def __str__(self) -> str:
        return "Name: {0.name}, Lives: {0.lives}, Level: {0._level}, Score {0.score}".format(
            self
        )



