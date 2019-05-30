from SlideState import SlideState
from queue import Queue, LifoQueue, PriorityQueue

class SlidePuzzleSolve:
    def __init__(self, start, p_vazio):
        self.start = SlideState(None, start, vazio=p_vazio)
        self.end = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]

    def bfs(self):
        if self.start.value == self.end:
            return self.start
        queue = Queue()
        visited = list()
        queue.put(self.start)
        while not queue.empty():
            # retira da pilha o mais externo para poder testar
            node = queue.get()
            # se este nó já foi visitado vai para o próximo da fila
            if node.value in visited:
                continue
            # se ele for o nó buscado o retorna
            if node.value == self.end:
                return node
            # senão o adiciona na lista de visited
            visited.append(node.value)
            # gera os estados filhos
            node.adjacent()
            # visita os nós filhos e os adiciona na fila
            for adj in node.adjacents:
                if adj.value not in visited:
                    queue.put(adj)
        return None

    def dfs(self):
        if self.start.value == self.end:
            return self.start
        stack, visited = LifoQueue(), list()
        stack.put(self.start)
        while not stack.empty():
            # retira da pilha o mais externo para poder testar
            node = stack.get()
            # se este nó já foi visitado vai para o próximo da pilha
            if node.value in visited:
                continue
            # se ele for o nó buscado o retorna
            if node.value == self.end:
                return node
            # senão o adiciona na lista de visited
            visited.append(node.value)
            # gera os estados filhos
            node.adjacent()
            # visita os nós filhos e os adiciona na pilha
            for adj in node.adjacents:
                if adj.value not in visited:
                    stack.put(adj)
        return None

    def dfs_limited(self, limit = 100):
        if self.start.value == self.end:
            return self.start
        stack, visited = LifoQueue(), list()
        stack.put(self.start)
        while not stack.empty():
            # retira da pilha o mais externo para poder testar
            node = stack.get()
            # se este nó já foi visitado ou se o nível dele é maior que o permitido
            # vai para o próximo da pilha
            if node.value in visited or node.cost > limit:
                continue
            # se ele for o nó buscado o retorna
            if node.value == self.end:
                return node
            # senão o adiciona na lista de visited
            visited.append(node.value)
            # gera os estados filhos
            node.adjacent()
            # visita os nós filhos e os adiciona na pilha
            for adj in node.adjacents:
                if adj.value not in visited:
                    stack.put(adj)
        return None
        
    def dfs_iterative(self, init_limit = 0, max_limit = 100, step_limit = 1):
        stack, visited = LifoQueue(), list()
        limit = init_limit
        while limit < max_limit:
            stack.put(self.start)
            visited.clear()
            while not stack.empty():
                # retira da pilha o mais externo para poder testar
                node = stack.get()
                # se este nó já foi visitado ou se o nível dele é maior que o permitido
                # vai para o próximo da pilha
                if node.value in visited or node.cost > limit:
                    continue
                # se ele for o nó buscado o retorna
                if node.value == self.end:
                    return node
                # senão o adiciona na lista de visited
                visited.append(node.value)
                # gera os estados filhos
                node.adjacent()
                # visita os nós filhos e os adiciona na pilha
                for adj in node.adjacents:
                    if adj.value not in visited:
                        stack.put(adj)
            limit += step_limit
        return None
		
    def ucs(self):
        if self.start.value == self.end:
            return self.start
        queue = PriorityQueue()
        visitados = list()
        queue.put((self.start.cost, self.start))
        while not queue.empty():
            # retira da pilha o mais externo para poder testar
            node = (queue.get())[-1]
            # se este nó já foi visitado vai para o próximo da pilha
            if node.value in visitados:
                continue
            # se ele for o nó buscado o retorna
            if node.value == self.end:
                return node
            # senão o adiciona na lista de visitados
            visitados.append(node.value)
            # gera os estados filhos
            node.adjacent()
            for adj in node.adjacents:
                if adj.value not in visitados:
                    queue.put((int(adj.cost), adj))
        return None
