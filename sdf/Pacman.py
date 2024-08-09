import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure
from stl import mesh
from tqdm import tqdm

import matplotlib.pyplot as plt

# Signed Distance Function (SDF) for a sphere
def sdf_sphere(point, radius, center):
    return np.linalg.norm(point - center) - radius

# Signed Distance Function (SDF) for a sphere
def sdf_box(point, radius, center):
    return np.linalg.norm(point - center) - radius

# Combine multiple SDFs into a union
def sdf_union(sdf_funcs, size, params):
    # Create a grid of points
    x = np.linspace(-size, size, 50)
    y = np.linspace(-size, size, 50)
    z = np.linspace(-size, size, 50)
    X, Y, Z = np.meshgrid(x, y, z)
    W = np.full_like(X, np.inf)

    total_points = len(x) * len(y) * len(z)
    progress_bar = tqdm(total=total_points, desc="Evaluating SDF")

    # Evaluate SDFs at each point and find the minimum distance
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(z)):
                point = np.array([x[i], y[j], z[k]])
                for sdf_func, param in zip(sdf_funcs, params):
                    W[i, j, k] = np.minimum(W[i, j, k], sdf_func(point, *param))
                progress_bar.update(1)
                
    progress_bar.close()        
    return X, Y, Z, W

# Export the SDF to an STL file
def export_to_stl(X, Y, Z, W, filename):
    # Generate the mesh using marching cubes algorithm
    verts, faces, _, _ = measure.marching_cubes(W, level=0)
    # Rescale the vertices to match the grid spacing
    verts = verts * (X[1, 0, 0] - X[0, 0, 0]) + X[0, 0, 0]
    verts = verts * (Y[0, 1, 0] - Y[0, 0, 0]) + Y[0, 0, 0]
    verts = verts * (Z[0, 0, 1] - Z[0, 0, 0]) + Z[0, 0, 0]

    # Create a mesh object and assign the vertices and faces
    mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = verts[f[j], :]

    # Save the mesh to an STL file
    mesh_data.save(filename)

# Plot the union of SDFs
def plot_sdf_union(sdf_funcs, size, params):
    # Generate the SDF grid
    X, Y, Z, W = sdf_union(sdf_funcs, size, params)

    # Find the zero level set (surface) of the SDF
    zero_level_set = np.where((np.abs(W) <= 0.01) & (np.abs(W) >= 0))
    
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[zero_level_set], Y[zero_level_set], Z[zero_level_set], c='blue', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Union of SDFs')
    ax.set_box_aspect([1, 1, 1])
    plt.show()

    # Export the SDF to an STL file
    export_to_stl(X, Y, Z, W, 'union_sdf.stl')

# Variables
center_sphere = np.array([0, 1, 0])
center_box = np.array([0, 0, 0])
radius_sphere = 1
size_box = np.array([1, 1, 1])

# Plotting
sdf_funcs = [sdf_sphere, sdf_box]
params = [(radius_sphere, center_sphere), (size_box, center_box)]
plot_sdf_union(sdf_funcs, 2, params)
