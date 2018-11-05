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

        if feature == POS:
            num = POSITIONS.index(num)
            num /= len(POSITIONS)

        elif feature == AGE:
            #Age required to play in NBA: 18
            #Oldest person to ever play: 46
            #That gives about a 30 year age range
            num = int(num)
            num -= 18
            num /= 30

        elif feature == GAM:
            num = int(num)
            num /= 82

        elif feature == PER:
            num = float(num) / 35

        elif feature == MP:
            num = float(num) / (82*48)

        elif feature == ORBP:
            num = float(num) / 100
        elif feature == DRBP:
            num = float(num) / 100
        elif feature == ASTP:
            num = float(num) / 100
        elif feature == STLP:
            num = float(num) / 100
        elif feature == BLKP:
            num = float(num) / 100
        return np.float32(num)