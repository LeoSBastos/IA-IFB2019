from SlidePuzzleSolve import SlidePuzzleSolve

# Imprime o resultado partindo do nó inicial até o final
def print_solution(state):
    if state is not None:
        print_solution(state.pai)
        print('{}\t{}'.format(state.move, state.value) )
    else:
        print('Move\tGame')

if __name__ == "__main__":
    a1 = [[1, 0, 2],[3, 4, 5],[6, 7, 8]]
    p1 = [0, 1]
    a3  = [[0, 3, 5],[2, 1, 6],[7, 8, 4]]
    p3  = [0, 0]

    sps1 = SlidePuzzleSolve(a1, p1)
    sps3 = SlidePuzzleSolve(a3, p3)
    print('\n\t\tBFS')
    print_solution(sps1.bfs())
    print('\n\t\tDFS')
    print_solution(sps1.dfs())
    print('\n\t\tUCS')
    print_solution(sps1.ucs())
    print('\n\t\tDFS Iterative')
    print_solution(sps1.dfs_iterative())