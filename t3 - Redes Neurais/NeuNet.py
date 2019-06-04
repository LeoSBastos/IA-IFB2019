#Importacao necessaria para o funcionamento do tensorflow
from __future__ import absolute_import, division, print_function, unicode_literals

#Importacao do tensorflow e do backend Keras
import tensorflow as tf
from tensorflow import keras

#Importacao do numpy e do matplotlib
import numpy as np
import matplotlib.pyplot as plt
#Importacao do random para a geracao de imagens aleatorias
import random
#Importacao para a criacao
import os
from pathlib import Path

class NeuNet:
    def __init__(self,train_x,train_label,test_x,test_label,epochs,ti,plot_linha=5, plot_coluna=5):
        self.plot_linha=plot_linha
        self.plot_coluna=plot_coluna
        self.train_x=train_x
        self.train_label=train_label
        self.test_x=test_x
        self.test_label=test_label
        self.epochs=epochs
        self.total_images=ti
        self.classes=range(10)
        self.train_x.shape
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28,28)),
            keras.layers.Dense(784,activation=tf.nn.relu),
            keras.layers.Dense(392,activation=tf.nn.sigmoid),
            keras.layers.Dense(392,activation=tf.nn.sigmoid),
            keras.layers.Dense(10, activation=tf.nn.sigmoid)
        ])
        self.model.compile(optimizer="adagrad",#"adam",
                    loss="sparse_categorical_crossentropy",
                    metrics=["accuracy"])
        self.model.fit(train_x,train_label,epochs=self.epochs)
        self.predictions = self.model.predict(test_x)

    
    def plot_image(self,i, predictions_array, true_label, img):
        predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)
    
        predicted_label = np.argmax(predictions_array)
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'

        plt.xlabel("IMG N{}: {} {:2.0f}% ({})".format(i,self.classes[predicted_label],
                                    100*np.max(predictions_array),
                                    self.classes[true_label]),
                                    color=color)

    def plot_value_array(self, i, predictions_array, true_label):
        predictions_array, true_label = predictions_array[i], true_label[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10), predictions_array, color="#a9a9a9")
        plt.ylim([0, 1]) 
        predicted_label = np.argmax(predictions_array)
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')

    def PlotGraph(self):
        num_images = self.plot_linha*self.plot_coluna
        my_path = os.path.abspath(__package__)
        for j in range(self.total_images):
            file_name = "figs/fig{}.png".format(j+1)
            plt.figure(figsize=(2*2*self.plot_coluna, 2*self.plot_linha))
            for i in range(num_images):
                aux=random.randint(0,len(self.test_x))
                plt.subplot(self.plot_linha, 2*self.plot_coluna, 2*i+1)
                self.plot_image(aux, self.predictions, self.test_label, self.test_x)
                plt.subplot(self.plot_linha, 2*self.plot_coluna, 2*i+2)
                self.plot_value_array(aux, self.predictions,self.test_label)
            p = Path(os.path.join(my_path,file_name)).resolve()
            plt.savefig(str(p))
