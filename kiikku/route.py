from ascent import Ascent

class Route:
    def __init__(self, route_id, name):
        self.id = u_id
        self.name = name

        self.ascent = []


    def add_ascent(self, ascent):
        if not isinstance(ascent, Ascent):
            raise Error("Invalid ascent")
        self.ascended.append(ascent)