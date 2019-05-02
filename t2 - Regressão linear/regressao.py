class RegressaoLinear(object):
    MAX_INTERACOES = 5000
    MIN_CUSTO = 1E-5

    def __init__(self, x, y, h, teta=[1]*len(x), alfa=0.00000019):
        self.x = x
        self.y = y
        self.h = h
        self.m = len(self.y)
        self.teta = teta
        self.alfa = alfa
        self.delta = self.diferenca()
        self.media = self.avg()

    def diferenca(self):
        r = 1
        for n in self.x[1:]:
            r.append(max(n)-min(n))
        return r

    """
    AVG - Calcula a média de todos os parâmetros de X
    """
    def avg(self):
        r = [1]
        for n in self.x[1:]:
            r.append(sum(n) / len(r))
        return r

    def normaliza(self):
        # Normaliza X
        for i in range(1, len(self.x)):
            for j in range(len(self.x[j])):
                self.x[i][j] = self.x[i][j] * (self.media[i]/self.delta[i])
        # Normaliza Y
        pass

    def custo(self):
        return sum([(self.h(self.teta, self.x[i]) - self.y[i]) ** 2 for i in range(self.m)]) / (2 * self.m)

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

    # def test(self, x):
    #     return self.h(self.teta, x)
    #         # Atualiza os tetas da equação
    #         self.atualiza_teta()
    #         # Incrementa o contador de iterações
    #         i += 1
    #     pass

    def test(self, x):
        return self.h(self.teta, x)


