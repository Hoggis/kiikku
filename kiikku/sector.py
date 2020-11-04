from route import Route

class Sector:
    def __init__(self, sector_id, name, lon, lat, route):
        self.sector_id = sector_id
        self.name = name
        self.lon = lon
        self.lat = lat
        self.routes = []

        if isinstance(route, Route):
            self.routes.append(route)
        elif isinstance(route, list):
            for entry in route:
                if not isinstance(entry, Route):
                    raise Error("Invalid Route")
            
            self.routes = route
        else:
            raise Error("Invalid route")

    def add_route(self, route):
        if not isinstance(route, Route):
            raise Error("Invalid route")
        self.routes.append(route)
