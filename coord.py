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

def coords_user():
    figures=library(1, 1, 1, False)
    new_shape_key = input("Enter the name of the new shape: ")
    new_shape_coordinates = []
    num_triangles = int(input(f"Enter the number of triangles for {new_shape_key}: "))
    for i in range(num_triangles):
        print(f"Enter coordinates for triangle {i + 1}:")
        triangle = []
        for j in range(3):
            vertex = input(f"Enter vertex {j + 1} (format: x,y,z) ADD COMAS: ")
            vertex = list(map(int, vertex.split(',')))
            triangle.append(vertex)
        new_shape_coordinates.append(triangle)

    # Add the new shape to the figures dictionary
    figures[new_shape_key] = new_shape_coordinates

    # Example usage
    print(f"Coordinates for {new_shape_key}: {figures[new_shape_key]}")

    object_3d = create_3d_object(figures[new_shape_key])
    export_stl(object_3d, 'output.stl')

def coords_standarized(x,y,z):
    center=[(-x+x)/2, (-y+y)/2, (-z+z)/2] #Center of the object
    #8 edges
    a=[-x,-y,-z]
    b=[-x,-y, z]
    c=[-x, y,-z]
    d=[-x, y, z]
    e=[ x,-y,-z]
    f=[ x,-y, z]
    g=[ x, y,-z]
    h=[ x, y, z]
    acdb=[  -x,         (-y+y)/2,   (-z+z)/2]
    abfe=[  (-x+x)/2,   -y,         (-z+z)/2]
    efgh=[  x,          (-y+y)/2,   (-z+z)/2]
    cdgh=[  (-x+x)/2,   y,          (-z+z)/2]
    bfdh=[  (-x+x)/2,   (-y+y)/2,   z       ]
    aceg=[  (-x+x)/2,   (-y+y)/2,   -z      ]
    print('Vertices created')
    return a, b, c, d, e, f, g, h, acdb, abfe, efgh, cdgh, bfdh, aceg, center


def library(x,y,z,standarized): #Center the object from the origin
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
    if standarized:
        selected_shape = input("Available shapes: "+ str(list(figures.keys()))+"\nEnter the name of the shape you want to create: ")
        return figures[selected_shape]
    else:
        return figures

def standarized(x,y,z):
    # Example usage
    object = library(x,y,z,True)

    # Create the 3D object
    object_3d = create_3d_object(object)

    # Export the 3D object as an STL file
    export_stl(object_3d, 'output.stl')

if __name__ == "__main__":
    print("User selected vertices or standarized vertices (U/S):")
    user = str(input())
    if user == 'U' or user == 'u':
        coords_user()
    elif user == 'S' or user == 's':
        print('Size of X:')
        x= int(input())
        print('Size of Y:')
        y= int(input())
        print('Size of Z:')
        z= int(input())
        standarized(x,y,z)
    else:
        print("Invalid input")