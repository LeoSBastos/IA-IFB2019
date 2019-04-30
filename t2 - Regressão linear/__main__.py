from regressao import RegressaoLinear as rl

def reader(file_name):
    # Lista com todos os Xs e Ys utilizados para o aprendizado
    x, y = [], []
    # Leitura do arquivo
    with open(file_name, 'r') as file:
        # Lê o arquivo e cria um vetor com todas as linhas dele
        linhas = file.read().split('\n')
        # Lê o número de colunas
        colunas = int(linhas[0][0])
        # Lista de X indo de X0 ate Xn-1
        x.append(colunas * list())
        # Leitura dos parâmetros, que começam na linha 6
        for l in linhas[6:]:
            c = l.split()
            for i in range(colunas+1):
                if i == colunas:
                    y.append(int(c[i]))
                else:
                    x[i].append(int(c[0]))
    return x, y
    
if __name__ == "__main__":
    x, y = reader('data1.txt')

    def h(teta, x): return sum([(teta[i]*x[i]) for i in range(len(x))])

    r = rl(x, y, h)
    #r.solve()

    #print(r.test([1, 2104, 3]))
    print(r.x, r.y)
