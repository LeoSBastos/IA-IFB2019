import argparse
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

def reader(file_name,n):
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
    return final, np.array(y)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description="Trabalho 3 de Inteligência Computacional - Treinamento de Redes Neurais")
    parser.add_argument("TRF", metavar="train_filename",
    type=str,nargs='?',default="train.csv",help="O nome do arquivo contendo as imagens de treino, default: train.csv")
    parser.add_argument("TRN",metavar="train_number",type=int,nargs='?',
    help="Número de imagens a serem treinadas")
    parser.add_argument("TSF", metavar="test_filename",
                        type=str, nargs='?', default="test.csv", help="O nome do arquivo contendo as imagens de teste, default: test.csv")
    parser.add_argument("TSN",metavar="test_number",type=int,nargs='?',
    help="Número de imagens a serem testadas")
    parser.add_argument("--epochs",metavar="epochs",type=int,nargs='?',default=5,
    dest="epochs",help="O número de iterações de treinamento, default: 5")
    parser.add_argument("--ti",metavar="total_images",type=int,nargs='?',default=1,
    dest="ti",help="O número de imagens de 5x5 figuras geradas, default: 1")
    args = parser.parse_args()
    # Chama a função para ler o arquivo e retornar os vetores X e Y
    train_x, train_label = reader(args.TRF,args.TRN)
    test_x, test_label = reader(args.TSF,args.TSN)
    
    #Crie a classe de Regressão Linear com os vetores x, y e a função custo C
    rede = NeuNet(train_x, train_label, test_x, test_label,args.epochs,args.ti)
    #Utiliza a função solve que atualiza os tetas e a função custo de acordo com o número de iterações que foram selecionadas.
    rede.PlotGraph()