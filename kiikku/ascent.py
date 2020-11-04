import datetime
from route import Route
from climber import Climber

class Ascent:
    def __init__(self, climber, route):
        if not isinstance(climber, Climber):
            raise Error("Invalid climber")
        if not isinstance(route, Route):
            raise Error("invalid route")

        self.climber = climber
        self.route = route
        self.grade = None
        self.style = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade

    def set_style(self, style):
        self.style = style
