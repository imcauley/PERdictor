import numpy as np
from Globals import *

class Player:
    # Selected Stats


    def __init__(self, name):
        self.S_STATS = [
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

        self.name = name
        self.stats = []

    def add_year(self, year, stats):
        stats = self._convert_stats(stats)
        self.stats.append(stats)

    def _convert_stats(self, stats):
        relevant = []

        for s in self.S_STATS:
            relevant.append(float(stats[s]))

        return relevant