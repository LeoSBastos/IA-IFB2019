from copy import deepcopy

class SlideState:
    def __init__(self, pai = None, value = [], vazio = [], cost = 0, move = 'Start'):
        self.pai = pai # SliderState
        self.value = value # [[], [], []]
        self.vazio = vazio # [X, Y]
        self.cost = cost
        self.adjacents = []
        self.move = move

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.move < other.move
    
    def adjacent(self):
        if len(self.adjacents) > 0:
            return 
        x0, y0 = self.vazio[1], self.vazio[0]
        #sobe
        if y0 > 0:
            aux = deepcopy(self.value)
            aux[y0][x0] = deepcopy(aux[y0 - 1][x0])
            aux[y0 - 1][x0] = 0
            temp = SlideState(self, aux, [y0 - 1, x0], cost=self.cost + 1, move='Up')
            if temp not in self.adjacents:
                self.adjacents.append(temp)
        #desce
        if y0 < 2:
            aux = deepcopy(self.value)
            aux[y0][x0] = aux[y0 + 1][x0]
            aux[y0 + 1][x0] = 0
            temp = SlideState(self, aux, [y0 + 1, x0], cost=self.cost + 1, move='Down')
            if temp not in self.adjacents:
                self.adjacents.append(temp)
        #esquerda
        if x0 > 0:
            aux = deepcopy(self.value)
            aux[y0][x0], aux[y0][x0 - 1] = aux[y0][x0 - 1], 0
            temp = SlideState(self, aux, [y0, x0 - 1], cost=self.cost + 1, move='Left')
            if temp not in self.adjacents:
                self.adjacents.append(temp)
        #direita
        if x0 < 2:
            aux = deepcopy(self.value)
            aux[y0][x0], aux[y0][x0 + 1] = aux[y0][x0 + 1], 0
            temp = SlideState(self, aux, [y0, x0 + 1], cost=self.cost + 1, move='Rigth')
            if temp not in self.adjacents:
                self.adjacents.append(temp)
        return self.adjacents
