"""
    TRABALHO 1
- GRUPO: Jerônimo Hermano (161057600021) e Leonardo Bastos(171057600008)
- Entrega pelo endereço de e-mail lucas.moreira@ifb.edu.br até às 23h55min do dia 14 de abril de 2019.

    MISSIONÁRIOS E CANIBAIS
- 3 missionários e 3 canibais de um lado do rio
- atravessar todos para o outro lado
- um barco que leva  ou 2 pessoas
- o número de missionários de um lado não pode ser menor do que o número de canibais
"""

class Estado:
    """
    Ideia do estado:
    - Estado será um vetor de duas posições, aonde a primeira indica a margem aonde está o barco
    - A segunda é um inteiro de até 4 digitos representando a disposição dos canibais e missionarios pelas margens
        >Unidade: Missionario do Lado B do rio
        >Dezena: Canibal do Lado B do rio
        >Centena: Missionario do Lado A do rio
        >Unidade de Milhar: Canibal do Lado A do rio
    """
    # Constantes para definição dos canibais e missionarios
    CANIBAL_A = 1000
    CANIBAL_B = 10
    MISSIONARIO_A = 100 
    MISSIONARIO_B = 1
    #Constantes para definição do estado atual da margem do rio aonde está o barco
    LADO_A = 1
    LADO_B = 0

    def __init__(self, state):
        self.state = state

    def move_canibais(self, qtd):
        # Verificação do lado que o barco está atualmente no rio
        if(self.state[0]==LADO_A):
            #Move os canibais de acordo com a posição do rio que eles estão e utilizazndo as constantes de disposição
            return [LADO_B,self.state[1]+qtd*CANIBAL_B-qtd*CANIBAL_A]
        else:
            return [LADO_A,self.state[1]+qtd*CANIBAL_A-qtd*CANIBAL_B]

    def move_missionarios(self, qtd):
        # Verificação do lado que o barco está atualmente no rio
        if(self.state[0]==LADO_A):
            #Move os missionarios de acordo com a posição do rio que eles estão e utilizazndo as constantes de disposição
            return [LADO_B,self.state[1]+qtd*MISSIONARIO_B-qtd*MISSIONARIO_A]
        else:
            return [LADO_A,self.state[1]+qtd*MISSIONARIO_A-qtd*MISSIONARIO_B]
    def isAlive(self):
        CA = self.state[1]//CANIBAL_A
        MA = (self.state[1]//MISSIONARIO_A) % 10
        CB = (self.state[1]//CANIBAL_B) % 10
        MB = self.state[1] % 10
        return not((CA>MA and MA != 0) or (CB>MB and MB != 0))

# Importa a estrutura de dados de pilha
from queue import LifoQueue
# Classe que conterá os algoritmos de solução dos algoritmos
class Solve:
    """
        DFS - DEPH-FIRST SEARCH
    """
    def dfs(self):
        # Caso o nó inicial seja o nó buscado ele o retorna sem ter que entrar a busca
        if self.start.value == self.end:
            return self.start
        # Pilha: utilizada para percorer o os nós da arvore de busca
        stack = LifoQueue()
        # Contendo os nós que já foram visitados
        visited = list()
        # Adiciona o nó inicial a lista de nós visitados
        stack.put(self.start)
        # Percorre os nós que da árvore
        while not stack.empty():
            # remove da pilha o mais externo para poder testar
            node = stack.get()
            # se este nó já foi visitado vai para o próximo da pilha
            if node.value in visited and node.:
                continue
            # se ele for o nó buscado o retorna
            if node.value == self.end:
                return node
            # senão o adiciona na lista de visited
            visited.append(node.value)
            # verifica se os missionarios estão vivos neste estado
            if if adj.isAlive():
                # gera os estados filhos
                node.adjacent()
                # visita os nós filhos e os adiciona na pilha
                for adj in node.adjacents:
                    # Adiciona os nós novos a pilha para que sejam visitados
                    if adj.value not in visited:
                        stack.put(adj)
        # Retorna None caso não consiga encontrar 
        return None
