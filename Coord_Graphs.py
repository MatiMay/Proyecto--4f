import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
from stl import mesh # type: ignore

graph3d = nx.Graph()
graphs = []

#Graphs
def Input_graphs():
    # Get the number of graphs from the user
    num_graphs = int(input("Enter the number of graphs: "))

    # Create the graphs based on user input
    for i in range(num_graphs):
        graph = nx.Graph()
        nodes = input(f"Enter the nodes for graph {i+1} (separated by spaces): ").split()
        num_edges = int(input(f"Enter the number of edges for graph {i+1}: "))
        edges = []
        for _ in range(num_edges):
            edge = input(f"Enter an edge (format: node1 node2) for graph {i+1}: ").split()
            edges.append(edge)
        graph.add_edges_from(edges)
        graph.add_edges_from(edges)
        graphs.append(graph)
    return graphs

def create_3d_graph(graphs):
    # Create the 3D graph
    for graph in graphs:
        # Add nodes from the current graph
        graph3d.add_nodes_from(graph.nodes())
        
        # Add edges from the current graph
        graph3d.add_edges_from(graph.edges())
    return graph3d

def plot_3dGraf():
    plt.subplot(1, len(graphs)+1, len(graphs)+1)
    nx.draw(graph3d, with_labels=True)
    plt.title('Graph 3D')

    plt.show()


#3D object
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

def coords_user():
    figures=library(1, 1, 1)
    new_shape_key = input("Enter the name of the new shape: ") # Example: 'triangle', 'pentagon', this name will appear in the figures dictionary 
    new_shape_coordinates = []
    num_triangles = int(input(f"Enter the number of triangles for {new_shape_key}: ")) # Triangles of faces from object
    for i in range(num_triangles):  #For each triangle/face
        print(f"Enter coordinates for triangle {i + 1}:")
        triangle = []
        for j in range(3):  #For each vertex of the triangle
            vertex = input(f"Enter vertex {j + 1} (format: x,y,z) ADD COMAS: ") # Input the coordinates of the vertex
            vertex = list(map(int, vertex.split(','))) # Split the input comas to 3 numbers
            triangle.append(vertex)
        new_shape_coordinates.append(triangle)

    figures[new_shape_key] = new_shape_coordinates # Add the new shape to the figures dictionary

    #print(f"Coordinates for {new_shape_key}: {figures[new_shape_key]}")

    object_3d = create_3d_object(figures[new_shape_key])
    print("Object created")
    export_stl(object_3d, 'output.stl')

def coords_standarized(x,y,z):
    a=[-x,-y,-z]
    b=[-x,-y, z]
    c=[-x, y,-z]
    d=[-x, y, z]
    e=[ x,-y,-z]
    f=[ x,-y, z]
    g=[ x, y,-z]
    h=[ x, y, z]
    center=[(-x+x)/2, (-y+y)/2, (-z+z)/2] #Center of the object
    cdgh=[  (-x+x)/2,   y,          (-z+z)/2]
    bfdh=[  (-x+x)/2,   (-y+y)/2,   z       ]
    aceg=[  (-x+x)/2,   (-y+y)/2,   -z      ]
    acdb=[  -x,         (-y+y)/2,   (-z+z)/2]
    abfe=[  (-x+x)/2,   -y,         (-z+z)/2]
    efgh=[  x,          (-y+y)/2,   (-z+z)/2]
    return a, b, c, d, e, f, g, h, acdb, abfe, efgh, cdgh, bfdh, aceg, center

def library(x,y,z): #Center the object from the origin
    a, b, c, d, e, f, g, h, acdb,abfe,efgh,cdgh,bfdh,aceg, center = coords_standarized(x, y, z)
    figures = {
    'cube': [
        [a, e, b],  # Triangle 1
        [b, e, f],  # Triangle 2 Face 1
        [b, h, d],  # Triangle 3
        [b, f, h],  # Triangle 4 Face 2
        [a, b, d],  # Triangle 5 
        [a, d, c],  # Triangle 6 Face 3
        [c, d, h],  # Triangle 7
        [c, h, g],  # Triangle 8 Face 4
        [a, c, g],  # Triangle 9
        [a, g, e],  # Triangle 10 Face 5
        [e, g, f],  # Triangle 11
        [f, g, h],  # Triangle 12 Face 6
    ],
    'triangle': [
        
        [b, a, e],  # Triangle 1
        [e, c, b],  # Triangle 2
        [e, a, c],  # Triangle 3
        [b, c, a]   # Triangle 4
    ]
}
    return figures


Input_graphs()#Graphs
graph3d = create_3d_graph(graphs)
plot_3dGraf()
print("\n\n\n coords ejecutados\n\n\n")

coords_user() #3d object
print("\n\n\n coords ejecutados\n\n\n")