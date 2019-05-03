from regressao import RegressaoLinear as rl


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
def reader(file_name):
    # Lista com todos os Xs e Ys utilizados para o aprendizado
    x, y = [], []
    # Leitura do arquivo
    with open(file_name, 'r') as file:
        # Lê o arquivo e cria um vetor com todas as linhas dele
        linhas = file.read().split('\n')
        # Lê o número de colunas
        colunas = int(linhas[0])
        # Lista de X indo de X0 ate Xn-1
        x.append( (colunas - 1) * list())
        # Leitura dos parâmetros, que começam na linha 6
        for l in linhas[6:]:
            # Particiona a linha em vetores
            c = l.split()
            # Percorre os vetores pelos ídices
            for i in range(colunas):
                # X0 - A coluna 0 é o index
                if i == 0:
                    x[0].append(int(c[0]))
                # XN com N > 0
                elif 0 < i < (colunas - 1):
                    x[i].append(int(c[i]))
                # Y - A última coluna é o 
                else:
                    y.append(int(c[i]))
    # retorna a matriz de valor X e os Y resultados
    return x, y

if __name__ == "__main__":
    # Chama a função para ler o arquivo e retornar os vetores X e Y
    x, y = reader('data.1.txt')
    
    # Funcção C: calcula o tamanho do peixe com base na idade e temperatura da agua
    def c(teta, x): return sum([(teta[i]*x[i]) for i in range(len(teta))])

    r = rl(x, y, c)
    #r.solve()
    #print(r.test([1, 2104, 3]))
    print(r.x, r.y)
