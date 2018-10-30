import csv
import re
import json
import numpy as np

from Player import Player


FILENAME = '../data/Seasons_Stats_without_blanks.csv'

def get_data():
    X = []
    Y = []

    raw = get_players()

    for name, data in raw.items():
        mat = np.asarray(data.stats)

        seasons,_ = mat.shape
        if seasons > 1:
            new_x = mat
            new_y = np.roll(new_x, -1, axis=0)

            new_x = np.delete(new_x, 0, axis=0)
            new_y = np.delete(new_y, -1, axis=0)

            X.append(new_x)
            Y.append(new_y)

    return X, Y

def get_players():
    data = {}

    with open(FILENAME) as f:
        reader = csv.reader(f)
        for row in reader:
            if (_valid_row(row)):

                index, year, player, *stats = row
                
                player = _clean_name(player)

                if player in data:
                    data[player].add_year(year, stats)

                else:
                    new_player = Player(player)
                    data[player] = new_player
                    data[player].add_year(year, stats)


    return data


def create_position_mapping():
    with open(FILENAME) as f:
        reader = csv.reader(f)
        next(reader, None)

        positions = [row[3] for row in reader]

    positions = list(set(positions))

    with open("../data/Position_Mapping.json", "w") as f:
        json.dump(positions, f, indent=2)


def _clean_name(name):
    name = re.sub(r'\*', '', name)
    return name


def _valid_row(row):
    # TODO only include TOT if exists

    if row[0] == 'Index':
        return False

    for stat in row:
        if stat == None:
            return False

        if stat == '':
            return False

    return True

if __name__ == '__main__':
    data = get_data()
    print(data['Kawhi Leonard'].stats)
