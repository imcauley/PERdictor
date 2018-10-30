import numpy as np
import keras
import tensorflow as tf
import Globals

class Model:
    def __init__(self):
        self.build_model()

    def build_model(self):
        self.model = keras.Sequential([
            keras.layers.SimpleRNN(64, activation=tf.nn.relu, input_shape=(None, len(Globals.FEATURES))),
            keras.layers.Dense(len(Globals.FEATURES))
        ])

        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def train_model():
        pass

    def test_model():
        pass


if __name__ == '__main__':
    m = Model()