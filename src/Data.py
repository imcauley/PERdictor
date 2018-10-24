import csv

from Player import Player


FILENAME = '../data/Seasons_Stats.csv'

def get_data():
    data = {}

    with open(FILENAME) as f:
        reader = csv.reader(f)
        for row, year, player, pos, *stats in reader:

            if player in data:
                data[player].add_year(year, stats)

            else:
                new_player = Player(player, pos)
                data[player] = new_player
                data[player].add_year(year, stats)


    return data


if __name__ == '__main__':
    data = get_data()

    print(data['Cliff Barker'].stats)