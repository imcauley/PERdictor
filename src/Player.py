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
        # TODO only take relevant stats

        relevant = []

        for s in S_STATS:
            relevant.append(float(stats[s]))

        pos = POSITIONS.index([POS])

        relevant.append(pos)

        return relevant