from typing import List, Tuple
import numpy as np # type: ignore
from stl import mesh # type: ignore

def create_3d_object(coordinates):
    # Create a numpy array from the coordinates
    vertices = np.array(coordinates)

    # Create a mesh object
    mesh_object = mesh.Mesh(np.zeros(vertices.shape[0], dtype=mesh.Mesh.dtype))
    for i, vertex in enumerate(vertices):
        mesh_object.vectors[i] = vertex
    return mesh_object

def export_stl(mesh_object, filename):
    # Export the mesh object as an STL file
    mesh_object.save(filename)



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
    out = []
    for i in lista:
        in1=coords[i[0]]
        in2=coords[i[1]]
        in3=coords[i[2]]
        out.append([in1,in2,in3])
        #print([in1,in2,in3])
    return out

def sacarIteraciones(caras):
    vistos= set()
    resultado= []
    for i in caras:
        if frozenset(i) not in vistos:
            resultado.append(i)
            vistos.add(frozenset(i))
    return resultado

def figure():
    """input("Vertices:\n")""" 
    """input("\nConections:\n")"""
    vertices: List[List[float]] = [
        [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
        [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1],
        [0, 0.618, 1.618], [0, 0.618, -1.618], [0, -0.618, 1.618], [0, -0.618, -1.618],
        [0.618, 1.618, 0], [0.618, -1.618, 0], [-0.618, 1.618, 0], [-0.618, -1.618, 0],
        [1.618, 0, 0.618], [1.618, 0, -0.618], [-1.618, 0, 0.618], [-1.618, 0, -0.618]
    ]
    connections: List[List[int]] = [
        [8, 12, 16, 2, 4], [12, 9, 13, 3, 0], [16, 10, 14, 3, 0], [14, 11, 7, 1, 2],
        [8, 18, 15, 6, 0], [9, 19, 7, 1, 4], [10, 18, 17, 7, 2], [11, 19, 15, 6, 3],
        [0, 10, 12, 14, 4], [1, 11, 13, 15, 5], [2, 8, 16, 18, 6], [3, 9, 14, 19, 7],
        [0, 8, 16, 18, 1], [1, 9, 17, 19, 5], [2, 10, 18, 16, 3], [3, 11, 19, 17, 7],
        [0, 2, 8, 10, 12], [6, 10, 18, 14, 4], [4, 6, 8, 12, 16], [5, 7, 9, 13, 15]
    ]
    return connections, vertices


if __name__=="__main__":

    ver= figure()[1]
    object=llamarIndice(sacarIteraciones(crearCaras(figure())),ver)
    object3D = create_3d_object(object)
    export_stl(object3D,"C:\\Users\\mamak\\3D Objects\\Output.stl")
    print("Objeto creado")