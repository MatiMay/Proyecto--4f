import numpy as np
from stl import mesh

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


def main(x,y,z): #Center the object from the origin
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

    # Example usage
    coordinates = figures['cube']

    # Create the 3D object
    object_3d = create_3d_object(coordinates)

    # Export the 3D object as an STL file
    export_stl(object_3d, 'output.stl')


if __name__ == "__main__":
    print("X :")
    x=int(input())
    print("Y :")
    y=int(input())
    print("Z :")
    z=int(input())
    main(x,y,z)