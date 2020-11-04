import datetime
from ascent import Ascent

class Climber:
    def __init__(self, first, last, nick, pwd, create_date):
        self.first_name = first
        self.last_name = last
        self.user_name = nick
        self.password = pwd
        self.create_date = datetime.now
        self.ascended = []

    def add_ascent(self, ascent):
        if not isinstance(ascent, Ascent):
            raise Error("Invalid ascent")
        self.ascended.append(ascent)