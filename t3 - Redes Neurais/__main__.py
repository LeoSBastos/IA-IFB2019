import numpy as np
import numpy.linalg as LA
from NeuNet import NeuNet

"""
O arquivo data.txt possui a seguinte formatação
 - A primeira linha informa o número de colunas nas linhas de dados
 - A segunda linha informa o número total de amostras
 - As linhas 3-6 indicam o significado de cada coluna na amostra de dados
 - Coluna 0: indice da linha, em seu lugar será salvo o valor 1 para X0
 - Coluna 2: idade do peixe, valor de X1
 - Coluna 3: temperatura da água em C°, valor de X2
 - Coluna 4: tamanho do peixe, Y
"""

def readerTrain(file_name,n):
    # Lista com todos os Xs e Ys utilizados para o aprendizado
    y = []
    # Leitura do arquivo
    with open(file_name, 'r') as file:
        # Lê o arquivo e cria um vetor com todas as linhas dele
        linhas = file.read().split('\n')
        # Lista de X indo de X0 ate Xn-1
        x = [[[] for i in range(28)] for i in range(n)]
        # Leitura dos parâmetros, que começam na linha 6
        for i,l in enumerate(linhas[1:]):
            # Particiona a linha em vetores
            c = l.split(",")
            # Percorre os vetores pelos ídices
            y.append(int(c.pop(0)))
            for j in range(28):
                for k in range(28):
                    x[i][j].append(int(c[28*j+k]))
    aux=np.array(x)
    final = np.empty([n,28,28])

    for i in range(len(aux)):
        final[i]=(aux[i]/LA.norm(aux[i]))
    # retorna a matriz de valor X e os Y resultados
    return final, y

def readerTest(file_name,n):
    # Lista com todos os Xs e Ys utilizados para o aprendizado
    # Leitura do arquivo
    with open(file_name, 'r') as file:
        # Lê o arquivo e cria um vetor com todas as linhas dele
        linhas = file.read().split('\n')
        # Lista de X indo de X0 ate Xn-1
        x= [[[] for i in range(28)] for i in range(n)]
        # Leitura dos parâmetros, que começam na linha 6
        for i,l in enumerate(linhas[1:]):
            # Particiona a linha em vetores
            c = l.split(",")
            # Percorre os vetores pelos ídices
            for j in range(28):
                for k in range(28):
                    x[i][j].append(int(c[28*j+k]))
    # retorna a matriz de valor X
    aux=np.array(x)
    final = np.empty([n,28,28])
    for i in range(len(aux)):
        final[i]=(x[i]/LA.norm(aux[i]))
    return final


if __name__ == "__main__":
    # Chama a função para ler o arquivo e retornar os vetores X e Y
    train_x, train_y = readerTrain('train.csv',42000)
    test_x = readerTest('test.csv',28000)
    
    #Crie a classe de Regressão Linear com os vetores x, y e a função custo C
    rede = NeuNet(train_x, train_y, test_x)
    #Utiliza a função solve que atualiza os tetas e a função custo de acordo com o número de iterações que foram selecionadas.
    rede.PlotGraph()