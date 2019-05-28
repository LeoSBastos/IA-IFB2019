from __future__ import absolute_import, division, print_function, unicode_literals

#tensor
import tensorflow as tf
from tensorflow import keras


import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

class NeuNet:
    def __init__(self,train_x,train_y,test_x,plot_linha=5, plot_coluna=5):
        self.plot_linha=plot_linha
        self.plot_coluna=plot_coluna
        self.train_x=train_x
        self.train_y=train_y
        self.test_x=test_x
        self.classes=range(10)
        self.train_x.shape
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28,28)),
            keras.layers.Dense(784,activation=tf.nn.sigmoid),
            keras.layers.Dense(392,activation=tf.nn.sigmoid),
            keras.layers.Dense(392,activation=tf.nn.sigmoid),
            keras.layers.Dense(10, activation=tf.nn.sigmoid)
        ])
        self.model.compile(optimizer="adam",
                    loss="sparse_categorical_crossentropy",
                    metrics=["accuracy"])
        self.model.fit(train_x,train_y,epochs=3)
        self.predictions = self.model.predict(test_x)

    def plot_image(self,i, predictions_array, img):
        predictions_array, img = predictions_array[i], img[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)

        predicted_label = np.argmax(predictions_array)
        plt.xlabel("{} {:2.0f}%".format(self.classes[predicted_label],
                                        100*np.max(predictions_array),
                                        color='black'))                            

    def plot_value_array(self,i, predictions_array):
        predictions_array = predictions_array[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10), predictions_array, color="#777777")
        plt.ylim([0, 1]) 
        self.predicted_label = np.argmax(predictions_array)
        thisplot[self.predicted_label].set_color('blue')

    def PlotGraph(self):
        num_images = self.plot_linha*self.plot_coluna
        my_path = os.path.abspath(__package__)
        for j in range(0,len(self.test_x),num_images):
            file_name = "figs/fig{}.png".format(j)
            plt.figure(figsize=(2*2*self.plot_coluna, 2*self.plot_linha))
            for i in range(num_images):
                plt.subplot(self.plot_linha, 2*self.plot_coluna, 2*i+1)
                self.plot_image(j+i, self.predictions, self.test_x)
                plt.subplot(self.plot_linha, 2*self.plot_coluna, 2*i+2)
                self.plot_value_array(j+i, self.predictions)
            p = Path(os.path.join(my_path,file_name)).resolve()
            plt.savefig(str(p))