import numpy as np
from Globals import *

class Player:
    # Selected Stats
    S_STATS = [
        GOA,
        MP,
        PER,
        TS,
        THPAR,
        FTR,
        ORB,
        DRB,
        AST,
        STL,
        BLK,
        WS,
        VORP,
        EFG,
    ]


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