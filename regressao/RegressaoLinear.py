class RegressaoLinear(object):
    MAX_INTERACOES  = 500000
    MIN_CUSTO       = 1E-5

    def delta(self):
        lstaux = [aux[1] for aux in self.x]
        lstaux2 = [aux[2] for aux in self.x]
        return [1,max(lstaux)-min(lstaux),max(lstaux2)-min(lstaux2)]

    def avg(self):
        lstaux = [aux[1] for aux in self.x]
        lstaux2 = [aux[2] for aux in self.x]
        return [1, sum(lstaux)/len(lstaux), sum(lstaux2)/len(lstaux2)]

    def __init__(self, x, y, h, teta = [1,1,1], alfa = 0.00000019):
        self.x = x
        self.y = y
        self.h = h
        self.m = len(self.y)
        self.teta = teta
        self.alfa = alfa
        self.delta = self.delta(self)
        self.avg = self.avg(self)

    def normaliza(self):
        # Normaliza X
        
        # Normaliza Y
        return
    def custo(self):
        return sum([(self.h(self.teta, self.x[i]) - self.y[i]) ** 2 for i in range(self.m)]) / (2 * self.m)

    def atualiza_teta(self):
        novo = list()
        for j in range(len(self.x[1])):
            aux = self.alfa
            aux *= sum([(self.h(self.teta, self.x[i]) - self.y[i]) * self.x[i][j]  for i in range(self.m)]) / self.m
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

    def test(self, x):
        return self.h(self.teta, x)
            # Atualiza os tetas da equação
            self.atualiza_teta()

            # Incrementa o contador de iterações
            i += 1
        pass

    def test(self, x):

        return self.h(self.teta, x)
