#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:46:12 2019
@author: Jeronimo Hermano e Leonardo Bastos
"""

#Importacao do objeto Carro
from carro import Carro 
#Importacao do objeto Cluster e os seus metodos de agrupamento 
from Cluster import Cluster
#Importacao da biblioteca prettytable para a impressao da tabela com os resultados
from prettytable import PrettyTable
#Importacao da bilioteca de estatistica do python para o calculo de media e desvio padrao
import statistics

"""
    Variáveis globais que são utilizadas tanto na normalização dos valores,
    quanto na desnormalização.
"""

media_carbono = 0.0
media_milhagem = 0.0
desvio_carbono = 0.0
desvio_milhagem = 0.0


"""
    Realiza a leitura do dataset, para cada linha é criado um objeto do tipo
    Carro, que é formado pelo modelo, carbono produzido, milhagem e a Classe, ou
    Centroid que este ocupa, este último é definido pelo procedimento de Cluster
"""
def leitura(arquivo):
    #Informa que usará a variável global tam
    global tam
    #Cria uma lista de carros, a qual sera retornada
    carros = list()
    #Abre o arquivo para leitura
    with open(arquivo, 'r') as file:
        #Divide o testo lido em linhas
        for linha in file.read().split('\n')[1:]:
            #Separa cada linha em modelo, carbono e milhagem
            modelo, carbono, milhagem = linha.split(',')
            #Adiciona um objeto Carro criado a partir da linha lida
            carros.append(Carro(modelo, carbono, milhagem))
    #Coloca a variavel tam com o valor igual a quantidadde de carros
    tam = len(carros)
    #Retorna o vetor de carros
    return carros

"""
    Normaliza os valores de milhagem e carbono dos carros da seguinte maneira
                    valor - média
    Normalizado = -----------------
                    desvio padrão
    Aplica a fórmula tanto em X quanto em Y.
"""
def normaliza(carros):
    #Indica que utilizará as variáveis globais
    global media_carbono
    global media_milhagem
    global desvio_carbono
    global desvio_milhagem
    #Vetor de X: carbono
    x = []
    #Vetor de Y: milhagem
    y = []
    #Popula vetores
    for c in carros:
        x.append(c.x)
        y.append(c.y)
    #Calculo da média
    media_carbono = statistics.mean(x)
    media_milhagem = statistics.mean(y)
    #Calculo o desvio padrão
    desvio_carbono = statistics.pstdev(x)
    desvio_milhagem = statistics.pstdev(y)
    #Aplica normalizacao: (valor - média) / desvio padrão
    for i in range(tam):
        carros[i].x = (carros[i].x - media_carbono) / desvio_carbono
        carros[i].y = (carros[i].y - media_milhagem) / desvio_milhagem
    #Retorna o vetor de carros normalizados
    return carros


"""
    Reverte o cálculo da normalização para apresentação dos centróides
    
    centroide = (valor normalizado * desvio padrão) - média
    
    Aplicando a fórmula tanto em X quanto em Y
"""
def desnormalizaCentroids(centroids):
    #Indica que utilizará as variáveis globais
    global media_carbono
    global media_milhagem
    global desvio_carbono
    global desvio_milhagem
    
    #Para cada centroid aplica a desnormalizacao
    for i in range(len(centroids)):
        centroids[i][0] = (centroids[i][0] * desvio_carbono) + media_carbono
        centroids[i][1] = (centroids[i][1] * desvio_carbono) + media_carbono
    
    #Retorna os centroid desnormalizados
    return centroids


"""
    Função principal
    - Ela é responsável pela chamada das funções que irão realizar a leitura do
    arquivo, processar seus dados com o algoritmo de Cluster e então imprimir o
    custo para cada caso de teste, imprimindo detalhadamente os custos do caso
    em que obtivermos o melhor resultado (análise manual)
"""
if __name__=="__main__":
    #Leitura dos dados do carro junto com a
    #Normalização dos dados
    carros_normalizado = normaliza(leitura("data.txt"))
    
    #Cria um objeto Pretty Table com as colunas abaixo e o alinhamento dos dados a esquerda
    tab1 = PrettyTable(["Numero de classes", "Custo Total"])
    tab1.align = 'l'
    #Inicia o teste com números variados de centróides para encontrar a que 
    #melhor se ajusta ao dataset
    for i in range(2,31):
        cl = Cluster(carros_normalizado,i)
        cl.solve()
        tab1.add_row([i,cl.custo])

    #Caso de teste que será impresso mais detalhadamente
    cl2 = Cluster(carros_normalizado,6)

    #Cria um objeto Pretty Table com as colunas abaixo e o alinhamento dos dados a esquerda
    tab_centroides = PrettyTable(["Classe", "Custo local", "Nodes","Coordenada X", "Coordenada Y"])
    tab_centroides.align = 'l'
    #Para cada centroid no teste mais detalhado sera desnormalizado
    #e adicionado na tabela
    for i, l in enumerate(cl2.solve(final=True)):
        cl2.centroid = desnormalizaCentroids(cl2.centroid)
        tab_centroides.add_row([l[0],l[1],l[2],cl2.centroid[i][0],cl2.centroid[i][1]])
    #Configuração da tabela de carros
    tab_carros = PrettyTable(["Modelo", "Centroid"])
    tab_carros.align = 'l'
    #Adicao das linhas da tabela de carros
    for c in cl2.Carros:
        tab_carros.add_row([c.modelo,c.classe])
    
    #Impressão da tabela de carros
    print(tab_carros)
    #Impressao da tabela de centroids
    print(tab_centroides)
