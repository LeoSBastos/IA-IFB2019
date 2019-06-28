#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:46:12 2019

@author: Jeronimo Hermano
"""

from carro import Carro 
from Cluster import Cluster
from prettytable import PrettyTable
import statistics

"""
    variáveis globais que são utilizadas tanto na normalização dos valores,
    quanto na desnormalização
"""
media_carbono = 0.0
media_milhagem = 0.0
desvio_carbono = 0.0
desvio_milhagem = 0.0



"""
    Realiza a leitura do dataset, para cada linha é criado um objeto do tipo
    Carro, que é formado pelo modelo, carbono produzido, milhagem e a Classe,
    este último é definido pelo procedimento de Cluster
"""
def leitura(arquivo):
    # informa que usará a variável globam tan
    global tam
    # cria uma lista de carros, a qual será retornada
    carros = list()
    # abre o arquivo para leitura
    with open(arquivo, 'r') as file:
        # divide o testo lido em linhas
        for linha in file.read().split('\n')[1:]:
            # separa cada linha em modelo, carbono e milhagem
            modelo, carbono, milhagem = linha.split(',')
            # adiciona um objeto Carro criado a partir da linha lida
            carros.append(Carro(modelo, carbono, milhagem))
    # 
    tam = len(carros)
    # retorna o vetor de carros
    return carros

"""
    Normaliza os valores de milhagem e carbono dos carros da seguinte maneira
                    valor - média
    normalizado = -----------------
                    desvio padrão
    Aplica a fórmula tanto em X quanto em Y.
"""
def normaliza(carros):
    # indica que utilizará as variáveis globais
    global media_carbono
    global media_milhagem
    global desvio_carbono
    global desvio_milhagem
    # vetor de X: carbono
    x = []
    # vetor de Y: milhagem
    y = []
    # popula vetores
    for c in carros:
        x.append(c.x)
        y.append(c.y)
    # cálcula da média
    media_carbono = statistics.mean(x)
    media_milhagem = statistics.mean(y)
    # calcula o desvio padrão
    desvio_carbono = statistics.pstdev(x)
    desvio_milhagem = statistics.pstdev(y)
#    desvio_carbono = statistics.pvariance(x)
#    desvio_milhagem = statistics.pvariance(y)
    # aplica normalização: (valor - média) / desvio padrão
    for i in range(tam):
#        print(carros[i].x, end = ' ')
        carros[i].x = (carros[i].x - media_carbono) / desvio_carbono
#        print(carros[i].x)
        carros[i].y = (carros[i].y - media_milhagem) / desvio_milhagem
    # retorna o vetor de carros normalizados
    return carros


"""
    Reverte o cálculo da normalização para apresentação dos centróides
    
    centroide = (valor normalizado * desvio padrão) - média
    
    Aplicando a fórmula tanto em X quanto em Y
"""
def desnormalizaCentroids(centroids):
    global media_carbono
    global media_milhagem
    global desvio_carbono
    global desvio_milhagem
    for i in range(len(centroids)):
        centroids[i][0] = (centroids[i] * desvio_carbono) + media_carbono
        centroids[i][1] = (centroids[i] * desvio_carbono) + media_carbono
    return centroids


"""
    Função principal
    - Ela é responsável pela chamada das funções que irão realizar a leitura do
    arquivo, processar seus dados com o algoritmo de Cluster e então imprimir o
    custo para cada caso de teste, imprimindo detalhadamente os custos do caso
    em que obtivermos o melhor resultado (análise manual)
"""
if __name__=="__main__":
    # Leitura dos dados do carro
    # Normalização dos dados
    carros_normalizado = normaliza(leitura("data.txt"))
    
    # Inicia o teste com números variados de centróides para encontrar a que 
    # melhor se ajusta ao dataset
    tab1 = PrettyTable(["Numero de classes", "Custo Total"])
    tab1.align = 'l'
    for i in range(2,31):
        cl = Cluster(carros_normalizado,i)
        cl.solve()
        tab1.add_row([i,cl.custo])

    # Caso de teste que será impresso mais detalhadamente
    cl2 = Cluster(carros_normalizado,5)
    
    tab_centroides = PrettyTable(["Classe", "Custo local", "Nodes"])#,"Coordenada X", "Coordenada Y"])
    tab_centroides.align = 'l'
    for l in cl2.solve(final=True):
        tab_centroides.add_row(l)
    # Configuração da tabela de carros
    tab_carros = PrettyTable(["Modelo", "Centroid"])
    tab_carros.align = 'l'
    for c in cl2.Carros:
        tab_carros.add_row([c.modelo,c.classe])
    
    # Impressão dos resultados
    #   Tabela com número de classes e o erro total de cada uma delas
#    print(tab1)
    #   Tabela de carros e a classe ao qual pertence
    #print(tab_carros)
    #   
    print(tab_centroides)
    #   Gráfico com os pontos iniciais dos carros e os pontos das centróides
#    cl2.plot()