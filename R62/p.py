from collections import deque

def bfs(grafo, inicio):

    visitados = set()
    cola = deque([inicio])
    resultado = []
    
    while cola:
        nodo_actual = cola.popleft()
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            resultado.append(nodo_actual)
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    cola.append(vecino)
    return resultado

def main():
    grafo1 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("Grafo 1:", grafo1)
    print("BFS desde A:", bfs(grafo1, 'A'))
    print("BFS desde C:", bfs(grafo1, 'C'))
    
    grafo2 = {
        'X': ['Y', 'Z'],
        'Y': ['Z', 'W'],
        'Z': [],
        'W': ['X']
    }
    print("\nGrafo 2:", grafo2)
    print("BFS desde X:", bfs(grafo2, 'X'))
    print("BFS desde W:", bfs(grafo2, 'W'))
    
    grafo3 = {
        '1': ['2', '3'],
        '2': ['4'],
        '3': [],
        '4': [],
        '5': [] 
    }
    print("\nGrafo 3:", grafo3)
    print("BFS desde 1:", bfs(grafo3, '1'))
    print("BFS desde 5:", bfs(grafo3, '5'))
    print("BFS desde X (no existe en el grafo):", bfs(grafo3, 'X'))

if `__name__`` == `"__main__"`:
    main()