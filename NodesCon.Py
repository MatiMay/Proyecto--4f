from typing import List, Tuple

def newcubegraph() -> Tuple[List[List[int]], List[List[int]]]:
    vertices: List[List[int]] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    
    connections: List[List[int]] = [[1, 2, 4], [0, 5, 3], [0, 3, 6], [2, 7, 1], [0, 5, 6], [4, 7, 1], [2, 4, 7], [3, 6, 5]]
    
    return connections, vertices

def newpyramidgraph() -> Tuple[List[List[int]], List[List[int]]]:
    vertices: List[List[int]] = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0.5, 0.5, 1]
    ]
    
    connections: List[List[int]] = [
        [1, 3, 4],
        [0, 2, 4],
        [1, 3, 4],
        [0, 2, 4],
        [0, 1, 2, 3]
    ]
    
    return connections, vertices

def newtetrahedrongraph() -> Tuple[List[List[int]], List[List[float]]]:
    # Definimos los vértices de un tetraedro.
    vertices: List[List[float]] = [
        [1, 1, 1],   # Vértice 0
        [-1, -1, 1], # Vértice 1
        [-1, 1, -1], # Vértice 2
        [1, -1, -1]  # Vértice 3
    ]
    
    # Definimos las conexiones (aristas) entre los vértices del tetraedro.
    connections: List[List[int]] = [
        [1, 2, 3], # Vértice 0 se conecta con 1, 2, 3
        [0, 2, 3], # Vértice 1 se conecta con 0, 2, 3
        [0, 1, 3], # Vértice 2 se conecta con 0, 1, 3
        [0, 1, 2]  # Vértice 3 se conecta con 0, 1, 2
    ]
    
    return connections, vertices

ver, con = newcubegraph()
print(ver,"\n", con)