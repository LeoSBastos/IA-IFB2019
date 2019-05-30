from Tabuleiro import tabuleiro
from random import random, randint
from math import floor

class ag():
    def __init__(self, t_populacao = 100, taxa_cruzamento = 0.5, taxa_mutacao = 2e-3, max_geracoes = 100, taxa_sobrevivencia = 0.4):
        self.t_populacao = t_populacao
        #self.taxa_cruzamento = taxa_cruzamento
        self.t_cross = floor(8 * taxa_cruzamento)
        #self.taxa_mutacao = taxa_mutacao
        self.max_geracoes = max_geracoes
        self.populacao = list()
        self.genemutados = (taxa_mutacao * t_populacao * 8)
        self.numerosobreviventes = floor(t_populacao * taxa_sobrevivencia)
		
    """
    Gera a população inicial
    """
    def gera_populacao(self):
        for i in range(self.t_populacao):
            self.populacao.append(tabuleiro())

    """
    Seleciona os sobreviventes da população atual
    """
    def selecao(self):
        self.populacao.sort()
        self.listasobreviventes = self.populacao[:self.numerosobreviventes]

    """
    Cruza os sobreviventes até completar a população
    """
    def cruzamento(self):
        t_populacao_atual = self.numerosobreviventes
		custo_total = 0
		for p in self.populacao:
			custo_total += p.custo
        # Até completar a populacao
        while t_populacao_atual < self.t_populacao:
            # escolhe A
            mae = list()
            # escolhe um B != A
            pai = list()
            # posicao inicial que pega dos genes de A
            p_mae = randint(0, 7 - self.t_cross)
            # cria item filho
            c = list()
            for i in range(8):
                if p_mae < i < self.t_cross + p_mae:
                    c.append(mae[i])
                else:
                    c.append(pai[i])

    """
    Altera alguns genes aleatórios, de indivíduos aleatórios, para valores aleatórios
    """
    def mutacao(self):
        for i in range(self.genemutados):
            self.populacao[randint(1, self.t_populacao)].queens[randint(0, 8)] = randint(0, 8)


    """
    Aplica os passos do algoritmo genético
    """
    def solve(self):
        geracao = 0
        # Cria a populacao original
        self.gera_populacao()
        # Evolução dos genes
        while self.populacao[0].custo != 0 and geracao < self.max_geracoes:
            # selecao
            self.selecao()
            # cruzamento
            # mutacao
            self.mutacao()
            geracao += 1
        # exibe o gene com o resultado
        print('# Geração {}: {} custo'.format(geracao, self.populacao[0].custo))
        self.populacao[0].print()
