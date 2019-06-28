#Importacao do math para o calculo de raiz
import math
#Importacao para gerar os eixos aleatorios das centroids iniciais
import random

#Classe com os metodos do agrupamento
class Cluster():
    #Recebe como parametro inicial: a lista de carros e o numero de centroids
    def __init__(self,carros,nodes):
        #Lista de carros
        self.Carros = carros
        #Numero de centroids
        self.knodes = nodes
        #Centroids inicias criadas de forma aleatoria
        self.centroid=[[random.uniform(-1,1),random.uniform(-1,1)] for i in range(self.knodes)]
        #Custo total
        self.custo = 0
        #Tamanho do vetor carros
        self.qtdCarros = len(self.Carros)

    #Calculo de distancia
    def distancia(self,carro,centroid):
        return math.sqrt((carro.x-centroid[0])**2 + (carro.y-centroid[1])**2)
    
    #Metodo que rotula os pontos
    def rotularPontos(self):
        #Percorre a lista de carros
        for i in range(self.qtdCarros):
            #Atribui a primeira distancia possivel como minima
            distmin = self.distancia(self.Carros[i], self.centroid[0])
            rotulo = 0
            #Percorre a lista de centroids
            for j in range(1, self.knodes):
                #Atribui a distancia com o centroid atual
                distatual = self.distancia(self.Carros[i], self.centroid[j])
                #Se a distancia atual for menor ou igual que a minima
                #Muda a distancia atual como minima e muda o rotulo com
                #o indice do centroid atual
                if distatual <= distmin:
                    distmin = distatual
                    rotulo = j    
            #Ao finalizar o percorrer muda o centroid do carro
            #de acordo com o rotulo
            self.Carros[i].classe = rotulo

    #Metodo que calcula o custo global
    def calcularCusto(self):
        custo = 0
        #Percorre a lista de carros
        for i in range(self.qtdCarros):
            #Soma no custo local a distancia de cada carro
            #com seu centroid
            custo += (self.distancia(self.Carros[i],self.centroid[self.Carros[i].classe]) ** 2)
        #Retorna a media ao dividir o custo local pela quantidade
        #de carros
        return (custo / self.qtdCarros)
    
    #Metodo de calcular o custo de cada centroid
    def calcularCustoCentroid(self):
        #Lista com o indice dos centroids, o custo do centroid e o numero de carros por centroids
        custos = [ [i,0, 0] for i in range(self.knodes)]
        #Quantidade de carros por centroids
        qtd = [0 for i in range(self.knodes)]

        #Percorre a lista de carros
        for i in range(self.qtdCarros):
            #Aumenta o custo do centroid de acordo com a distancia do carro atual para o seu centroid
            custos[self.Carros[i].classe][1] += (self.distancia(self.Carros[i],self.centroid[self.Carros[i].classe]) ** 2)
            #Adiciona esse carro ao numero de carros do centroid dele
            qtd[self.Carros[i].classe] += 1
        
        #Percorre a lista de centroids
        for i in range(self.knodes):
            #Se for maior que zero, para não trabalhar com divisão por 0
            if qtd[i] > 0:
                #Custos vai se dividir com a quantidade para ter-se uma media
                custos[i][1] /= qtd[i]
            #Atribui a quantidade para a lista custos
            custos[i][2] = qtd[i]
        
        #Retorna custos
        return custos

    def atualizarCentroids(self):
        #Lista para as somas de x e y de cada carro dentro do seu centroid
        somas = [[0,0] for i in range(self.knodes)]
        #Lista de quantidade de carros por centroid
        qtd = [0 for i in range(self.knodes)]

        #Percorre a lista de carros
        for i in range(self.qtdCarros):
            #Adiciona o x para o vetor soma no indice de seu proprio centroid
            somas[self.Carros[i].classe][0] += self.Carros[i].x
            #Adiciona o y para o vetor soma no indice de seu proprio centroid
            somas[self.Carros[i].classe][1] += self.Carros[i].y
            #Adiciona o carro a quantidade para seu proprio centroid
            qtd[self.Carros[i].classe] += 1
        
        #Percorre a lista de centroids
        for i in range(self.knodes):
            #Verificacao para nao ter divisao por 0
            if qtd[i] != 0:
                #Atribui o centroid como a media dos eixos dos seus carros
                self.centroid[i]=[(somas[i][0]/qtd[i]),(somas[i][1]/qtd[i])]

    def solve(self,final=False):
        #Loop para iterar ate o custo ser igual a iteracao passada
        while True:
            #Utiliza-se dos métodos na seguinte ordem
            #1-Primeiro Rotula
            #2-Calcula o custo atual
            #3-Atualiza as Centroids
            self.rotularPontos()
            custo = self.calcularCusto()
            self.atualizarCentroids()
            #Se o custo dessa iteracao for igual do da passada quebra o loop
            if self.custo == custo:
                break
            #Atualiza o custo global com o custo dessa iteracao
            self.custo = custo
        #Se receber o valor Final como true calcula o custo por centroid e retorna a lista
        if final:
            return self.calcularCustoCentroid()
        #Se nao retorna nulos
        else:
            return None
