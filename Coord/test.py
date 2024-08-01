from stl import mesh
import numpy as np

# Define the 8 vertices of a unit cube
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Define the 12 triangles composing the cube
faces = np.array([
    [0, 3, 1],
    [1, 3, 2],
    [0, 4, 7],
    [0, 7, 3],
    [4, 5, 6],
    [4, 6, 7],
    [1, 5, 4],
    [1, 2, 5],
    [2, 6, 5],
    [2, 3, 6],
    [3, 7, 6],
    [1, 0, 4]
])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[face[j], :]

# Save the mesh to file
cube.save('cube.stl')
