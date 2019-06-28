import math
import random
import matplotlib.pyplot as plt

class Cluster():
    def __init__(self,carros,nodes):
        self.Carros = carros
        self.knodes = nodes
        self.centroid=[[random.uniform(-1,1),random.uniform(-1,1)] for i in range(self.knodes)]
        self.custo = 0
        self.qtdCarros = len(self.Carros)

    def distancia(self,carro,centroid):
        return math.sqrt((carro.x-centroid[0])**2 + (carro.y-centroid[1])**2)
    
    def rotularPontos(self):
        for i in range(self.qtdCarros):
            distmin = self.distancia(self.Carros[i], self.centroid[0])
            rotulo = 0
            
            for j in range(1, self.knodes):
                distatual = self.distancia(self.Carros[i], self.centroid[j])
                
                if distatual <= distmin:
                    distmin = distatual
                    rotulo = j    
            
            self.Carros[i].classe = rotulo

    def calcularCusto(self):
        custo = 0
        for i in range(self.qtdCarros):
            custo += (self.distancia(self.Carros[i],self.centroid[self.Carros[i].classe]) ** 2)
        return (custo / self.qtdCarros)
        
    def calcularCustoCentroid(self):
        custos = [ [i,0, 0] for i in range(self.knodes)]
        qtd = [0 for i in range(self.knodes)]

        for i in range(self.qtdCarros):
            custos[self.Carros[i].classe][1] += (self.distancia(self.Carros[i],self.centroid[self.Carros[i].classe]) ** 2)
            qtd[self.Carros[i].classe] += 1
        
        for i in range(self.knodes):
            if qtd[i] > 0:
                custos[i][1] /= qtd[i]
            custos[i][2] = qtd[i]
        return custos

    def atualizarCentroids(self):
        somas = [[0,0] for i in range(self.knodes)]
        qtd = [0 for i in range(self.knodes)]

        for i in range(self.qtdCarros):
            somas[self.Carros[i].classe][0] += self.Carros[i].x
            somas[self.Carros[i].classe][1] += self.Carros[i].y
            qtd[self.Carros[i].classe] += 1
        
        for i in range(self.knodes):
            if qtd[i] != 0:
                self.centroid[i]=[(somas[i][0]/qtd[i]),(somas[i][1]/qtd[i])]

    def solve(self,final=False):
        while True:
            self.rotularPontos()
            custo = self.calcularCusto()
            self.atualizarCentroids()
            if self.custo == custo:
                break
            self.custo = custo
        if final:
            return self.calcularCustoCentroid()
        else:
            return None
    
    def plot(self):
        x=[]
        y=[]
        x1 = []
        y1 = []
        for i in range(self.qtdCarros):
            x.append(self.Carros[i].x)
            y.append(self.Carros[i].y)
        for i in range(self.knodes):
            x1.append(self.centroid[i][0])
            y1.append(self.centroid[i][1])
        plt.scatter(x,y, s = 10, color='r')
        plt.scatter(x1,y1, s = 10, color='b')
        plt.show()