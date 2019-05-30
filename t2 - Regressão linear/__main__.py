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
    y = []
    # Leitura do arquivo
    with open(file_name, 'r') as file:
        # Lê o arquivo e cria um vetor com todas as linhas dele
        linhas = file.read().split('\n')
        # Lê o número de colunas
        colunas = int(linhas[0])
        # Lista de X indo de X0 ate Xn-1
        x= [[] for i in range(colunas - 1)]
        # Leitura dos parâmetros, que começam na linha 6
        for l in linhas[6:]:
            # Particiona a linha em vetores
            c = l.split()
            # Percorre os vetores pelos ídices
            for i in range(colunas):
                # X0 - A coluna 0 é o index
                if i == 0:
                    x[0].append(1)
                # XN com N > 0
                elif 0 < i < (colunas - 1):
                    x[i].append(int(c[i]))
                # Y - A última coluna é o 
                else:
                    y.append(int(c[i]))
    # retorna a matriz de valor X e os Y resultados
    return x, y

#Utilizando esse modulo externo para criacao de uma tabela ASCII com os dados de resultado
from prettytable import PrettyTable

#Classe dedicada para a impressao
class Impressao:
    def __init__(self, r):
        #Colocando uma variável para fácil acesso da Regressão
        self.r = r

    #Método para impressão dos tetas
    def TabTeta(self):
        #Criacao de uma variavel da biblioteca externa que recebe como parametro o nome das colunas
        Tabela = PrettyTable(["Tetas"])
        #Metodo para adicionar linhas de acordo com o numero de colunas com as variaveis dadas
        Tabela.add_row([self.r.teta])
        return Tabela

    #Método para a impressão dos Y resultantes
    def TabResultado(self):
        #Criacao de uma variavel da biblioteca externa que recebe como parametro o nome das colunas
        Tabela = PrettyTable(["Comprimento do Peixe(mm)"])
        #Metodo para adicionar linhas de acordo com o numero de colunas com as variaveis dadas
        Tabela.add_row([self.r.yFinal])
        return Tabela

if __name__ == "__main__":
    # Chama a função para ler o arquivo e retornar os vetores X e Y
    x, y = reader('data_1.txt')
    
    # Função C: calcula o tamanho do peixe com base na idade e temperatura da agua
    def c(teta, x): return sum([(teta[i]*x[i]) for i in range(len(teta))])
    
    #Crie a classe de Regressão Linear com os vetores x, y e a função custo C
    r = rl(x, y, c)
    #Utiliza a função solve que atualiza os tetas e a função custo de acordo com o número de iterações que foram selecionadas.
    r.solve()
    #Imprime os tetas
    print(Impressao(r).TabTeta())
    #String input para usar no loop e nos cálculos
    s = input("Digite o valor da Temperatura e da Idade separados por espaço ou digite sair para sair: ")
    while s.lower() != "sair":
        #Separando as váriaveis da string do input
        t,i = (int(x) for x in s.split())
        #Coloca os seguintes valores de X para tentar calcular 
        r.calculaY([1,t,i])
        #Imprime o y resultante
        print(Impressao(r).TabResultado())
        s = input("Digite o valor da Temperatura e da Idade separados por espaço ou digite sair para sair: ")