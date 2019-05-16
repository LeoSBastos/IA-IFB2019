from random import shuffle

class tabuleiro():
    
    def __init__(self, queens = None, qtd = 8):
        # dimensão do tabuleiro
        self.qtd = qtd
        # Caso base, é utilizado para criar a primeira geração
        if queens is None:
            queens = range(qtd)
            shuffle(queens)
        # Disposição das rainhas no tabuleiro
        #   - posicao: coluna
        #   - valor: liinha
        self.queens = queens
        # Calcula o custo da disposição atual tabuleiro
        self.calc_custo()

    def __lt__(self, outro):
        return (self.custo  < outro.custo)

    # função que calcula o custo do tabuleiro atual
    def calc_custo(self):
        self.custo = 0
        # colunas
        for rainhaA in range(self.qtd):
            # linhas
            for rainhaB in range(rainhaA, self.qtd):
                # Contabiliza os pares de rainhas que podem se atacar
                # e realiza um ataque horizontal ou um diagonal
                if  rainhaA != rainhaB and (self.queens[rainhaA] == self.queens[rainhaB] or
                    abs(self.queens[rainhaA] - self.queens[rainhaB]) == abs(/rainhaB - rainhaA)):
                    self.custo += 1

    def print(self):
        # colunas
        for coluna in range(self.qtd):
            # linhas
            for linha in range(self.qtd):
                if self.queens[coluna] == linha:
                    print('#', end=' ')
                else:
                    print('-', end=' ')
            print('')