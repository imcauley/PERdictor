import numpy as np
import keras
import tensorflow as tf

import Globals
from Data import get_data, get_player

class Model:
    def __init__(self, load=False):
        self.filepath = '../models/PER_model'

        if load:
            self.model = keras.models.load_model(self.filepath)
        else:
            self.build_model()


    def build_model(self):
        self.model = keras.Sequential([
            keras.layers.LSTM(64, activation=tf.nn.relu, input_shape=(28, len(Globals.FEATURES)), return_sequences=True),
            keras.layers.Dense(len(Globals.FEATURES))
        ])

        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def get_data(self):
        return get_data()

    def train_model(self, test_perc=0.2):
        x, y = self.get_data()

        if test_perc:
            test_len = int(len(x) * test_perc)

            test_x = x[:test_len]
            test_y = y[:test_len]
            train_x = x[test_len:]
            train_y = y[test_len:]

        else:
            train_x, train_y = map(list, zip(*data))

        history = self.model.fit(train_x, train_y, epochs=3)

        if test_perc:
            test = self.model.evaluate(test_x, test_y)
        else:
            test = 0.0

        self.model.save(self.filepath)

        return test


if __name__ == '__main__':
    m = Model()
    m.train_model()