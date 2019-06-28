class Cluster():
    def __init__(self,carros):
        self.Carros = carros
        self.custo = 0
        self.qtdCarros = len(self.Carros)

    def rotularPontos(self):

        for i in range(self.qtdCarros):
            distmin = 9999999999
            rotulo = -1
            
            for j in range(self.knodes):
                distatual = self.distancia(self.Carros[i],self.centroid[j])
                
                if distatual < distmin:
                    distmin = distatual
                    rotulo = j    
            
            self.Carros[i][j].classe = rotulo

    def calcularCusto(self):
        custo = 0
        for i in range(self.qtdCarros):
            custo += (self.distancia(self.Carros[i],self.centroid[self.Carros[i].classe]) ** 2)
        return (custo / self.qtdCarros)
        
    def calcularCustoCentroid(self):
        custos = [0 for i in range(self.knodes)]
        for i in range(self.qtdCarros):
            custo += (self.distancia(self.Carros[i],self.centroid[self.Carros[i].classe]) ** 2)
        return (custo / self.qtdCarros)


    def atualizarCentroids(self):
        somas = [[0,0] for i in range(self.knodes)]
        qtd = [0 for i in range(self.knodes)]

        for i in range(self.qtdCarros):
            somas[self.Carros[i].classe][0] += self.Carros[i].x
            somas[self.Carros[i].classe][1] += self.Carros[i].y
            qtd[self.Carros[i].classe] += 1
        
        for i in range(self.knodes):
            self.centroid[i]=[(somas[i][0]/qtd[i]),(somas[i][1]/qtd[i])]

    def solve(self):
        while True:
            self.rotularPontos()
            custo = self.calcularCusto()
            self.atualizarCentroids()
            if self.custo == custo:
                return self.calcularCustoCentroid() 
            self.custo = custo