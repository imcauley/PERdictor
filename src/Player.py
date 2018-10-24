import numpy as np

class Player:
    # Important Stats:
    # G
    # MP
    # PER
    # TS%
    # 3PAr
    # FTr
    # ORB%
    # DRB%
    # AST%
    # STL%
    # BLK%
    # WS
    # VORP
    # eFG%


    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.stats = np.empty([14,1])

    def add_year(self, year, stats):
        self.stats[year] = stats