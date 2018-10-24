class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.stats = {}

    def add_year(self, year, stats):
        self.stats[year] = stats