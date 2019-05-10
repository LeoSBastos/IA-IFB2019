from math import log, exp

class RegressaoLinear(object):
    # Número máximo de vezes que será aplicada a regressao linear
    MAX_INTERACOES = 100000
    # Custo mínimo, é uma das condições de parada do método solve()
    MIN_CUSTO = 1E-5

    def __init__(self, x, y, h, alfa=1E-7, normaliza = False, lineariza = False):
        self.x = x # Matriz de variáveis para aprendizado X
        self.y = y # Matriz de resultado para aprendizado X
        self.h = h # Funcao de hipótese
        self.m = len(self.y) # Quantidade de amostras
        self.teta = [1]*len(self.x)# Constantes da função: que serão otmizados pela regressao
        self.alfa = alfa # Taxa de aprendizagem
        #Utilizadas para decidir se vai ou não ser normalizado e/ou linearizado a regressão
        self.normaliza = normaliza 
        self.lineariza = lineariza
        #Chama os métodos criados para normalizar os valores
        if self.normaliza:
            self.x = self.normalizarX(self.x)
            self.y = self.normalizarY(self.y)
        # Chama os métodos criados para linearizar os valores
        if self.lineariza:
            self.x = self.linearizarX(self.x)
            self.y = self.linearizarY(self.y)
    """
    NORMALIZAR - Normaliza os valores de uma matriz
     - A normalização é aplicada linha a linha
     - Vi' = (Vi - MEDIAi) / DELTAi
    """
    def normalizarX(self, x):
        self.deltaX = []
        self.mediaX = []
        # Para todas as linhas de X
        for i in x:
                # calcula a media de cada parametro
                self.mediaX.append(sum(i) / self.m)
                # calcula a variacao de cada parametro
                self.deltaX.append(max(i) - min(i))
        # Para cada linha de X
        for i in range(1, len(x)):
            # Normaliza cada item da linha
            for j in range(self.m):
                x[i][j] = (x[i][j] - self.mediaX[i]) / self.deltaX[i]
        return x

    def normalizarY(self, y):
        # calcula a media do Y
        self.mediaY = sum(y) / self.m
        # calcula a variacao do Y
        self.deltaY = max(y) - min(y)
        # Para cada valor de Y
        for i in range(len(y)):
            # Normaliza cada item de Y
            y[i] = (y[i] - self.mediaY) / self.deltaY
        return y

    def linearizarX(self, x):
        # Para cada linha de X
        for i in range(1, len(x)):
            # Lineariza cada item da linha
            for j in range(self.m):
                if x[i][j] > 0:
                    x[i][j] = log(x[i][j])
                elif x[i][j] < 0:
                    x[i][j] = -log(abs(x[i][j]))
        return x

    def linearizarY(self, y):
        # Para cada valor de Y
        for i in range(len(y)):
            # Lineariza cada item de Y
            if y[i] > 0:
                y[i] = log(y[i])
            elif y[i] < 0:
                y[i] = -log(abs(y[i]))
        return y

    """
    CUSTO - Calcula o custo total para os testes com os atuais valores de TETA
     J = SUM( H(teta, x) - Y ) / 2M
    """
    def custo(self):
        c = 0
        # Percorre os M itens da amostra
        for i in range(self.m):
            # Passa como parametros a variável teta e uma lista com todos os Xji
            # e depois subtrai o Yi
            #   - i: linha do caso de teste
            #   - j: índice do X (x0, x1, x2, etc)
            c += (self.h(self.teta, [self.x[j][i] for j in range(len(self.x))]) - self.y[i]) ** 2
        return c / (2 * self.m)

    """
    """
    def atualiza_teta(self):
        # NOVO TETA: variável usada pois é não se pode alterar o teta até calcular todos so novos valores
        novo = list()
        # Calcula um novo valor para cada TETA
        # t é o índice de teta e o de x
        for t in range(len(self.teta)):
            # Variável auxiliar utilizada para calcular o novo TETAi: inica em 0
            aux = 0
            # Para todos os casos de teste
            # i -> índice do caso de teste (0 a m-1)
            for i in range(self.m):
                # Incrementa em (H(teta, x) - Y) para cada caso de teste
                # Forja o vetor X pegando as K colunas de uma i linha
                # E por fim subtrai Yi * Xi, para o X de mesmo índice que TETAi
                aux += (self.h(self.teta, [self.x[j][i] for j in range(len(self.x))]) - self.y[i]) * self.x[t][i]
            # É multiplicada pela taxa de aprendizado
            aux *= self.alfa
            # e dividido pela quantidade de elementos
            aux /= self.m
            # Por fim o valor de AUX é retirado de TETAi
            aux = self.teta[t] - aux
            # Adiciona TETAi a lista de novos testas
            novo.append(aux)
        # A lista de TETA recebe os NOVOS valores
        # print(self.teta)
        self.teta = novo

    """
    SOLVE: aplica a regressão linear para encontrar os parâmetros TETA que melhor se ajustam
     - Realiza um número máximo de interações delimitado por MAX_INTERACOES 
    """
    def solve(self):
        i = 0
        while i < self.MAX_INTERACOES:
            # Calcula o custo atual
            custo = self.custo()
            # Encerra os loops caso o custo seja suficientemente pequeno
            if custo < self.MIN_CUSTO:
                break
            # Atualiza os tetas da equação
            self.atualiza_teta()
            # Incrementa o contador de iterações
            i += 1
        pass

    # Função que possibilita realizar teste com a funçãoe criada a partir da regressão
    def calculaY(self, x):
        #Verifica se foi normalizado para normalizar os valores de X e então "desnormalizar" o valor de y
        if self.normaliza:
            for i in range(1,len(x)):
                x[i] = (x[i] - self.mediaX[i]) / self.deltaX[i]
            self.yFinal = (self.h(self.teta, x) * self.deltaY) + self.mediaY
        else:
            self.yFinal = self.h(self.teta,x)
        #Verifica se foi linearizado para depois usar exponencial elevado a y para conseguir o valor final
        if self.lineariza:
            self.yFinal = exp(self.yFinal)