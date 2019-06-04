#Biblioteca utilizada para pegar os argumentos do programa
import argparse

#Bibliotecas do numpy como um todo e a bilioteca de álgebra linear para o calculo da norma
import numpy as np
import numpy.linalg as LA

#Importando a classe do arquivo criado para a rede Neural
from NeuNet import NeuNet

"""
O arquivo train.csv e teste.csv possui a seguinte formatacao:
 - A primeira linha indicam o significado de cada coluna na amostra de dados
 - A segunda linha até a ultima possui a seguinte formatacao dos valores, separados com ",":
    - Coluna 1: indica o dígito que foi desenhado pelo usuário
    - Coluna 2-785: valor de cor do pixel
"""
#Funcao de leitura de arquivo que recebe o nome do arquivo como parametro
def reader(file_name):
    # Lista com todos os labels dentro do arquivo dado
    label = []
    # Leitura do arquivo
    with open(file_name, 'r') as file:
        # Lê o arquivo e cria um vetor com todas as linhas dele
        linhas = file.read().split('\n')
        # Retira a primeira linha pois nao se usa ela
        linhas.pop(0)
        # Calcule o numero de linhas para a criacao da matriz
        n=len(linhas)
        # Matriz tridimensional contendo n matrizes de 28x28
        x = [[[] for i in range(28)] for i in range(n)]
        # Leitura dos parametros, utilizando enumerate para receber o indice e o item da lista ao mesmo tempo
        for i,l in enumerate(linhas):
            # Particiona a linha para um vetor de valores
            c = l.split(",")
            # Retira o valor da primeira coluna para a lista de "labels"
            label.append(int(c.pop(0)))
            #Percorre as 28 linhas de cada uma das matrizes
            for j in range(28):
                #Percorre as 28 coluna de cada uma das matrizes
                for k in range(28):
                    #Adiciona na matriz i de linha j os 28 valores da linha i do arquivo
                    x[i][j].append(int(c[28*j+k]))
    #Cria um ndarray do numpy auxiliar para o calculo da norma
    aux=np.array(x)
    #Cria o ndarray final para armazenamento da matriz normalizada
    final = np.empty([n,28,28])

    #Para cada linha de aux
    for i in range(len(aux)):
        #Se calcula a sua norma
        final[i]=(aux[i]/LA.norm(aux[i]))
    # retorna a matriz de valores normalizados e um ndarray dos valores de "labels"
    return final, np.array(label)



if __name__ == "__main__":
    #Criacao da variavel de analise dos argumentos
    parser = argparse.ArgumentParser(
    description="Trabalho 3 de Inteligência Computacional - Treinamento de Redes Neurais")
    #Adiciona o argumento com o nome do arquivo de treino
    parser.add_argument("TRF", metavar="train_filename",
    type=str,nargs='?',default="train.csv",help="O nome do arquivo contendo as imagens de treino, default: train.csv")
    #Adiciona o argumento com o nome do arquivo de teste
    parser.add_argument("TSF", metavar="test_filename",
                        type=str, nargs='?', default="test.csv", help="O nome do arquivo contendo as imagens de teste, default: test.csv")
    #Adiciona o argumento opcional com o numero de epocas com o valor padrao 5
    parser.add_argument("--epocas",metavar="epocas",type=int,nargs='?',default=5,
    dest="epocas",help="O numero de epocas, default: 5")
    #Adiciona o argumento opcional com o numero de imagens 5x5 a serem geradas
    #com o valor padrao 1
    parser.add_argument("--ti",metavar="total_images",type=int,nargs='?',default=1,
    dest="ti",help="O numero de imagens de 5x5 figuras geradas, default: 1")
    #Recupera os argumentos recebidos
    args = parser.parse_args()
    # Chama a funcao para ler o arquivo e retornar as matrizes de imagem e de "labels" de
    # treino e de teste, enviando como parametro o argumento de nome respectivo
    train_x, train_label = reader(args.TRF)
    test_x, test_label = reader(args.TSF)
    
    #Crie a classe de Redes Neurais recebendo como parametro
    # a matriz de imagem e de labels de treino e de teste, o numero de epochs e 
    # o numero de imagens dados por argumento
    rede = NeuNet(train_x, train_label, test_x, test_label,args.epocas,args.ti)
    
    #Utiliza a funcao para gerar as imagens e os gráficos de barra e salvar em
    #arquivos
    rede.PlotGraph()
