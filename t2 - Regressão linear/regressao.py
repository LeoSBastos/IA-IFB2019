class RegressaoLinear(object):
    # Número máximo de vezes que será aplicada a regressao linear
    MAX_INTERACOES = 5000
    # Custo mínimo, é uma das condições de parada do método solve()
    MIN_CUSTO = 1E-5

    def __init__(self, x, y, h, teta=[1]*len(x), alfa=0.00000019, normaliza = True):
        self.x = x # Matriz de variáveis para aprendizado X
        self.y = y # Matriz de resultado para aprendizado X
        self.h = h # Funcao de hipótese
        self.m = len(self.y) # Quantidade de amostras
        self.teta = teta # Constantes da função: que serão otmizados pela regressao
        self.alfa = alfa # Taxa de aprendizagem
        if normaliza:
            self.x = self.normalizar(x)
            self.y = self.normalizar(y)

    """
    NORMALIZAR - Normaliza os valores de uma matriz
     - A normalização é aplicada linha a linha
     - Vi' = (Vi - MEDIAi) / DELTAi
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
                v[i][j] = (v[i][j] - media[i]) / delta[i]
        return v
    """
    CUSTO - Calcula o custo total para os testes com os atuais valores de TETA
     J = SUM( H(teta, x) - Y ) / 2M
    """
    def custo(self):
        c = 0
        # Peercorre os M itens da amostra
        for i in range(self.m):
            # Passa como parametros a variável teta e uma lista com todos os Xji
            # e depois subtrai o Yi
            #   - i: linha do caso de teste
            #   - j: índice do X (x0, x1, x2, etc)
            c += (self.h(self.teta, [self.x[j][i] for j in range(self.x)]) - self.y[i]) ** 2
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
                aux += (self.h(self.teta, [self.x[j][i] for j in range(self.x)]) - self.y[i]) * self.x[t][i]
            # É multiplicada pela taxa de aprendizado
            aux *= self.alfa
            # e dividido pela quantidade de elementos
            aux /= self.m
            # Por fim o valor de AUX é retirado de TETAi
            aux = self.teta[t] - aux
            # Adiciona TETAi a lista de novos testas
            novo.append(aux)
        # A lista de TETA recebe os NOVOS valores
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
    def test(self, x):
        return self.h(self.teta, x)
