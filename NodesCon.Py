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

def sacarIteraciones(caras):
    vistos= set()
    resultado= []
    for i in caras:
        if frozenset(i) not in vistos:
            resultado.append(i)
            vistos.add(frozenset(i))
    return resultado

def crearCaras(objeto):
    con, ver = objeto
    caras=[]

    for i in range(len(con)):
        for j in range(len(ver)):
            if j in con[i]:
                for k in range(len(ver)):
                    if k!=j and k in con[i]:
                        caras.append([i,j,k])
    return caras 

def llamarIndice(lista, coords):
    
    #in1: list[int]=[], in2: list[int]=[], in3: list[int]=[]
    out: list[list[list[int]]]=[]
    for i in lista:
        in1=coords[i[0]]
        in2=coords[i[1]]
        in3=coords[i[2]]
        out.append([in1,in2,in3])
        #print([in1,in2,in3])
    return out
        
con, ver = newcubegraph()

#print("1:  "+str(sacarIteraciones(crearCaras(newcubegraph()))))
#print("\n")
#print("2: "+ str(llamarIndice(sacarIteraciones(crearCaras(newcubegraph())),ver)))
#print("\n")