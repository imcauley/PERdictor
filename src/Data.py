import csv
import re
import json

from Player import Player


FILENAME = '../data/Seasons_Stats_without_blanks.csv'

def get_data():
    data = {}

    with open(FILENAME) as f:
        reader = csv.reader(f)
        for row in reader:
            if (_valid_row(row)):

                index, year, player, pos, *stats = row
                
                player = _clean_name(player)

                if player in data:
                    data[player].add_year(year, stats)

                else:
                    new_player = Player(player, pos)
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

    return True

if __name__ == '__main__':
    data = get_data()
    print(data['Kawhi Leonard'].stats)
