from sector import Sector
class Crag():
    def __init__(self, id, name, lat, lon, sector):
        self.id = id
        self.name = name
        self.lat =lat
        self.long = lon
        self.sectors = []

        if isinstance(sector, Sector):
            self.sectors.append(sector)
        elif isinstance(sector, list):
            for entry in list:
                if not isinstance(sector, Sector):
                    raise Error("Invalid sector")
            self.sectors = sector
        else:
            raise Error("Invalid sector")

    def add_sector(self,sector):
        if not isinstance(sector, Sector):
            raise Error("Invalid sector")
        self.sectors.append(sector)

        

        
