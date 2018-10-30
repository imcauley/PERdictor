import numpy as np
from Globals import *

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = []

    def add_year(self, year, stats):
        stats = self._convert_stats(stats)
        self.stats.append(stats)

    def _convert_stats(self, stats):
        relevant = []

        for f in FEATURES:
            stat = self._normalize(stats[f], f)
            relevant.append(stat)

        return relevant

    def _normalize(self, num, feature):
        #TODO age
        #TODO games
        #TODO pos

        return np.float32(num)