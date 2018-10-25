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
        self.stats = {}

    def add_year(self, year, stats):
        stats = self._convert_stats(stats)
        self.stats[year] = stats

    def _convert_stats(self, stats):
        # TODO convert strings to floats
        # TODO only take relevant stats
        # TODO encode Pos

        stats = [(stats[5])]
        return stats