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
#Importacao para a criacao do arquivo
import os
from pathlib import Path

class NeuNet:
    def __init__(self,train_x,train_label,test_x,test_label,epochs,ti,plot_linha=5, plot_coluna=5)
        #Numero de linhas e colunas(imagem e grafico de barras e considerado uma coluna)
        #da imagem que foram desenhadas
        self.plot_linha=plot_linha
        self.plot_coluna=plot_coluna
        #Matriz de imagens e "labels" de treino
        self.train_x=train_x
        self.train_label=train_label
        #Matriz de imagens e "labels" de teste
        self.test_x=test_x
        self.test_label=test_label
        #Numero de epocas
        self.epochs=epochs
        #Numero de imagens de 5x5
        self.total_images=ti
        #Classes dos numeros que foram desenhados
        self.classes=range(10)
        #Modelo de rede neural com 1 camada inicial de 784 com ativacao relu,
        #com 2 camadas ocultas e 1 de saida com ativacao sigmoid
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28,28)),
            keras.layers.Dense(784,activation=tf.nn.relu),
            keras.layers.Dense(392,activation=tf.nn.sigmoid),
            keras.layers.Dense(392,activation=tf.nn.sigmoid),
            keras.layers.Dense(10, activation=tf.nn.sigmoid)
        ])
        #Propriedade de compilaçao com a funcao de custo Categorical Crossentropy e otimizador de Gradiente Adaptivo
        self.model.compile(optimizer="adagrad",
                    loss="sparse_categorical_crossentropy",
                    metrics=["accuracy"])
        #Treina o modelo de acordo com o número de épocas
        self.model.fit(train_x,train_label,epochs=self.epochs)
        #Preve o modelo com o test
        self.predictions = self.model.predict(test_x)

    
    def plot_image(self,i, predictions_array, true_label, img):
        #Recebe a lista de previsoes, o label verdadeiro e a matriz 28x28 do indice i 
        predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
        #Cria uma imagem sem grid e com "labels" de x e y vazios
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        #Gera a imagem a partir da matriz
        plt.imshow(img, cmap=plt.cm.binary)
        #Retorna o indice do maior valor, ou seja, o indice da classe prevista
        predicted_label = np.argmax(predictions_array)
        #Se acertou a cor e azul, se nao e vermelho
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'
        #Coloca como legenda no seguinte formato, e.g. IMGN1805: 3 70,58% 3
        plt.xlabel("IMG N{}: {} {:2.0f}% ({})".format(i,self.classes[predicted_label],
                                    100*np.max(predictions_array),
                                    self.classes[true_label]),
                                    color=color)

    def plot_value_array(self, i, predictions_array, true_label):
        #Recebe a lista de previsoes, o label verdadeiro do indice i 
        predictions_array, true_label = predictions_array[i], true_label[i]
        #Cria uma imagem sem grid e com "labels" de x e y vazios
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        #Cria um grafico de barras com as 10 classes utilizando os valores da lista de previsao para colocar 
        #o tamanho das barras
        thisplot = plt.bar(range(10), predictions_array, color="#a9a9a9")
        #Atribui os valores de inicio e final do eixo Y
        plt.ylim([0, 1]) 
        #Retorna o indice do maior valor, ou seja, o indice da classe prevista
        predicted_label = np.argmax(predictions_array)
        #Atribui a cor vermelha para o label previsto e se ele for certo atribui azul por cima
        #Se não atribui os dois separados
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')

    def PlotGraph(self):
        #Numero de figuras por imagem, usando linha * coluna
        num_images = self.plot_linha*self.plot_coluna
        #Retorna o caminho absoluto da área de trabalho
        my_path = os.path.abspath(__package__)
        #Um laço de repeticao iterando o numero de imagens totais
        for j in range(self.total_images):
            #Cria o nome do arquivo da imagem
            file_name = "figs/fig{}.png".format(j+1)
            #Cria uma figura com o tamando para cada coluna e linha
            plt.figure(figsize=(2*2*self.plot_coluna, 2*self.plot_linha))
            #Um laço de repeticao iterando o numero de figuras
            for i in range(num_images):
                #Gera um numero aleatorio aux para gerar a imagem da matriz de indice aux
                aux=random.randint(0,len(self.test_x))
                #Cria uma subfigura dentro da figura princiapl
                plt.subplot(self.plot_linha, 2*self.plot_coluna, 2*i+1)
                #Gera a figura
                self.plot_image(aux, self.predictions, self.test_label, self.test_x)
                #Cria uma subfigura dentro da figura princiapl
                plt.subplot(self.plot_linha, 2*self.plot_coluna, 2*i+2)
                #Gera o grafico de barras
                self.plot_value_array(aux, self.predictions,self.test_label)
            #Cria um caminho p utilizando uma biblioteca que gera o caminho de acordo com o SO,
            #unindo o caminho absoluto com o nome do arquivo
            p = Path(os.path.join(my_path,file_name)).resolve()
            #Gera a imagem no caminho p
            plt.savefig(str(p))
