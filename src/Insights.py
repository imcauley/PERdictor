import numpy as np
import matplotlib.pyplot as plt
import Data

def plot_single_stat(data, index, player):
    stats = data[player].stats
    
    x = []
    y = []

    for year, stat in stats.items():
        x.append(year)
        y.append(float(stat[index]))

    plt.plot(x,y, 'ro')
    plt.show()

def test_plot():
    x = [0.1,0.2,0.3]
    y = [10,20,30]
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    data = Data.get_data()
    plot_single_stat(data, 0, 'Kyle Lowry')
