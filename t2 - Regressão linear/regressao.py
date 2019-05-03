class RegressaoLinear(object):
    MAX_INTERACOES = 5000
    MIN_CUSTO = 1E-5

    def __init__(self, x, y, h, teta=[1]*len(x), alfa=0.00000019, normaliza = True):
        self.x = x # Matriz de variáveis para aprendizado X
        self.y = y # Matriz de resultado para aprendizado X
        self.h = h # Funcao de hipótese
        self.m = len(self.y) # Quantidade de amostras
        self.teta = teta # Constantes da função: que serão otmizados pela regressão
        self.alfa = alfa # Taxa de aprendizagem
        if normaliza:
            self.x = self.normalizar(x)
            self.y = self.normalizar(y)

    """
    NORMALIZAR - Normaliza os valores de uma matriz
     - A normalização é aplicada linha a linha
    """
    def normalizar(self, v):
        delta = list()
        media = list()
        # Para todas as linhas de V
        for i in v:
            # calcula a media de cada parametro
            media.append(sum(i) / m)
            # calcula a variacao de cada parametro
            delta.append(max(i) - min(i))
        # Para cada linha de V
        for i in range(1, len(v)):
            # Normaliza cada item da linha
            for j in range(m):
                # Vi' = (Vi - MEDIAi) / DELTAi
                v[i][j] = (v[i][j] - media[i]) / delta[i]
        return v
    """
    CUSTO - Calcula o custo total para os testes com os atuais valores de TETA
     J = SUM( H(teta, x) - Y ) / 2M
    """
    def custo(self):
        c = 0
        # sum([(self.h(self.teta, self.x[i]) - self.y[i]) ** 2 for i in range(self.m)])
        for i in range(self.m):
            c += (self.h(self.teta, [self.x[i][j] for j in range(self.x)]) - self.y[i]) ** 2
        return c / (2 * self.m)

    def atualiza_teta(self):
        novo = list() 
        for j in range(len(self.x[1])):
            aux = self.alfa
            aux *= sum([(self.h(self.teta, self.x[i]) - self.y[i])
                        * self.x[i][j] for i in range(self.m)]) / self.m
            aux = self.teta[j] - aux
            novo.append(aux)
        print(novo)
        self.teta = novo

    def solve(self):
        i = 0
        while i < self.MAX_INTERACOES:
            # Calcula o custo atual
            custo = self.custo()
            # Para os loops caso o custo seja suficientemente pequeno
            if custo < self.MIN_CUSTO:
                break
            # Atualiza os tetas da equação
            self.atualiza_teta()
            # Incrementa o contador de iterações
            i += 1
        pass

    # Função que possibilita realizar teste com a funçãoe criada a partir da regressão
    def test(self, x):
        return self.h(self.teta, x)