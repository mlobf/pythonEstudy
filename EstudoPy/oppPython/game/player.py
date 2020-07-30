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
        score = level + 1000

    def _get_lives(self):  # getter for lives
        return self._lives

    def _set_lives(self, lives):  # setter for lives
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can not be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can be less then one")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property  # Getter for score
    def score(self):
        return self._score

    @score.setter # Setter for score
    def score(self, score):
        self._score = score

    def __str__(self) -> str:
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(
            self
        )
