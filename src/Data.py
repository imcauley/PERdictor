import csv

from Player import Player


FILENAME = '../data/Seasons_Stats.csv'

def get_data():
    data = {}

    with open(FILENAME) as f:
        reader = csv.reader(f)
        for *row in reader:
            if (_valid_row(row)):

                index, year, player, pos, *stats = row
                if player in data:
                    data[player].add_year(year, stats)

                else:
                    new_player = Player(player, pos)
                    data[player] = new_player
                    data[player].add_year(year, stats)


    return data

def _valid_row(row):
    return True

if __name__ == '__main__':
    data = get_data()

    print(data['Cliff Barker'].stats)