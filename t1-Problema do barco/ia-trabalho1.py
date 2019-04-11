"""
    TRABALHO 1
- GRUPO: Jerônimo Hermano (161057600021) e Leonardo Bastos(171057600008)
- Entrega pelo endereço de e-mail lucas.moreira@ifb.edu.br até às 23h55min do dia 14 de abril de 2019.

    MISSIONÁRIOS E CANIBAIS
- 3 missionários e 3 canibais de um lado do rio
- atravessar todos para o outro lado
- um barco que leva  ou 2 pessoas
- o numero de missionários de um lado não pode ser menor do que o numero de canibais
"""

class Estado:
    """
    Ideia do estado:
    - Estado será um vetor de 5 posições, aonde a primeira indica a margem aonde está o barco
    - As outras quatro indicam quantos canibais e missionários estam em cada margem seguindo a seguinte ordem de indice i
        >i=1: Canibal do Lado A
        >i=2: Missionario do Lado A
        >i=3: Canibal do Lado B
        >i=4: Missionario do Lado B
    """
    # Constantes para definição dos indices do lado do barco, dos canibais e missionarios de cada lado
    LADO_BARCO = 0
    CANIBAL_A = 1
    MISSIONARIO_A = 2 
    CANIBAL_B = 3
    MISSIONARIO_B = 4
    #Constantes para definição do estado atual da margem do rio aonde está o barco
    LADO_A = 1
    LADO_B = 0
    
    def __init__(self, state = [LADO_A,3,3,0,0], father = None, cost = 0, movimento = "Start"):
        self.state = state
        # Adicionando o no pai para mostrar o caminho
        self.father = father
        # Vetor que armazena as ramificações do estado atual
        self.adjacents = []
        # Distância do movimento da raiz ate o no atual
        self.cost = cost
        # Movimento que foi utilizado para a criação do no atual
        self.movimento = movimento

    def move(self, qtd_canibais, qtd_missionarios):
        # Verificação do lado que o barco está atualmente no rio
        if self.state[0] == self.LADO_A:
            #Move os canibais e missionarios de acordo com a posição do rio que eles estão e utilizazndo o vetor de estados
            return [self.LADO_B, self.state[self.CANIBAL_A]-qtd_canibais, self.state[self.MISSIONARIO_A]-qtd_missionarios,
            self.state[self.CANIBAL_B]+qtd_canibais,self.state[self.MISSIONARIO_B]+qtd_missionarios]
        else:
            return [self.LADO_A, self.state[self.CANIBAL_A]+qtd_canibais, self.state[self.MISSIONARIO_A]+qtd_missionarios,
            self.state[self.CANIBAL_B]-qtd_canibais,self.state[self.MISSIONARIO_B]-qtd_missionarios]
    
    def isAlive(self,state):
        #Verifica se tem mais canibais que missionarios em qualquer lado do rio, tirando a exceção de quando não tem missionarios
        return not((state[self.CANIBAL_A]>state[self.MISSIONARIO_A] and state[self.MISSIONARIO_A] != 0) or 
        (state[self.CANIBAL_B]>state[self.MISSIONARIO_B] and state[self.MISSIONARIO_B] != 0))
    
    def __eq__(self,other):
        #Utilizado na verificacao se um no foi visitado antes
        return self.state == other.state
    
    def __lt__(self, other):
        #Utilizado para prioritizar o custo
        return self.cost < other.cost

    def adjacent(self):
        #Nao deixa recriar filhos
        if len(self.adjacents) > 0:
            return
        #Verifica se esta no lado A
        if self.state[self.LADO_BARCO] == self.LADO_A:
            #Move 2 Canibais da margem A para B somente se houver quantidade suficiente de canibais
            if self.state[self.CANIBAL_A] > 1:
                aux = self.move(2, 0)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"2 canibais vao de A para B"))
            #Move 2 Missionarios da margem A para B somente se houver quantidade suficiente de missionarios
            if self.state[self.MISSIONARIO_A] > 1:
                aux = self.move(0, 2)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"2 missionarios vao de A para B"))
            #Move 1 Canibal e 1 Missionario da margem A para B somente se houver quantidade suficiente de canibais e missionarios
            if self.state[self.CANIBAL_A] > 0 and self.state[self.MISSIONARIO_A] > 0:
                aux = self.move(1, 1)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"1 canibal e 1 missionario vao de A para B"))
            #Move 1 Canibal da margem A para B somente se houver quantidade suficiente de canibais
            if self.state[self.CANIBAL_A] > 0:
                aux = self.move(1, 0)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"1 canibal vai de A para B"))
            #Move 1 Missionario da margem A para B somente se houver quantidade suficiente de missionarios
            if self.state[self.MISSIONARIO_A] > 0:
                aux = self.move(0, 1)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"1 missionario vai de A para B"))
        #Se o Barco estiver na margem B
        else:
            #Move 2 Canibais da margem B para A somente se houver quantidade suficiente de canibais
            if self.state[self.CANIBAL_B] > 1:
                aux = self.move(2, 0)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"2 canibais vao de B para A"))
            #Move 2 Missionarios da margem B para A somente se houver quantidade suficiente de missionarios
            if self.state[self.MISSIONARIO_B] > 1:
                aux = self.move(0, 2)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"2 missionarios vao de B para A"))
            #Move 1 Canibal e 1 Missionario da margem B para A somente se houver quantidade suficiente de canibais e missionarios
            if self.state[self.CANIBAL_B] > 0 and self.state[self.MISSIONARIO_B] > 0:
                aux = self.move(1, 1)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"1 canibal e 1 missionario vao de B para A"))
            #Move 1 Canibal da margem B para A somente se houver quantidade suficiente de canibais
            if self.state[self.CANIBAL_B] > 0:
                aux = self.move(1, 0)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"1 canibal vai de B para A"))
            #Move 1 Missionario da margem B para A somente se houver quantidade suficiente de missionarios
            if self.state[self.MISSIONARIO_B] > 0:
                aux = self.move(0, 1)
                if self.isAlive(aux):
                    self.adjacents.append(Estado(aux, self, self.cost+1,"1 missionario vai de B para A"))
        

# Importa a estrutura de dados de pilha
from queue import PriorityQueue
# Classe que conterá os algoritmos de solução dos algoritmos
class Solve:
    def __init__(self):
        #Estado inicial
        self.start = Estado()
        #Estado final
        self.end = [0,0,0,3,3]
    
    
    
    """
        UCS - UNIFORM COST SEARCH
    """
    def ucs(self):
        # Caso o nó inicial seja o nó buscado ele o retorna sem ter que entrar a busca
        if self.start.state == self.end:
            return self.start
        # Fila priotária: utilizada para percorer os nós da arvore de busca e ordenando eles por ordem de custo
        queue = PriorityQueue()
        # Contendo os nós que já foram visitados
        visited = list()
        # Adiciona o nó inicial a lista de nós visitados
        queue.put((self.start.cost,self.start))
        # Percorre os nós que da árvore
        while not queue.empty():
            # remove da fila priotária o mais externo para poder testar
            node = queue.get()[1]
            # se este nó já foi visitado vai para o próximo da fila priotária
            if node.state in visited:
                continue
            # se ele for o nó buscado o retorna
            if node.state == self.end:
                return node
            #senão o adiciona na lista de visited
            visited.append(node.state)
            #gera os estados filhos
            node.adjacent()
            #visita os nós filhos e os adiciona na fila priotária
            for adj in node.adjacents:
                #Adiciona os nós novos a fila priotária para que sejam visitados
                if adj.state not in visited:
                    queue.put((adj.cost,adj))
        # Retorna None caso não consiga encontrar 
        return None

#Utilizando esse modulo externo para criacao de uma tabela ASCII com os dados de resultado
from prettytable import PrettyTable

#Classe dedicada para a impressao
class Impressao:
    #Criacao de uma variavel da biblioteca externa que recebe como parametro o nome das colunas
    Tabela = PrettyTable(["Indice","Canibais A","Missionarios A","/","Canibais B","Missionarios B","Movimento"])
    #Indice que está dentro da Tabela
    i=1
    #Funcao recursiva para adicionar na tabela que recebe o no final do resultado como parametro
    def create_table(self,node):
        #Continuar ate chegar no pai inicial que e nulo
        if node is not None:
            #A funcao se chama recursivamente enviando o pai como parametro
            self.create_table(node.father)
            #Metodo para adicionar linhas de acordo com o numero de colunas
            #com as variaveis dadas
            self.Tabela.add_row([self.i,node.state[1],node.state[2],"/",node.state[3],node.state[4],node.movimento])
            self.i+=1
        else:
            #Se chegar no final ele começa a adicionar o certos
            return None

#Parte de inicializacao do codigo
#Inicia a classe de resolucao
teste = Solve().ucs()
#Imprime a tabela dada por meio do metodo de impressao
impressao = Impressao()
impressao.create_table(teste)
tabela = impressao.Tabela
print(tabela)