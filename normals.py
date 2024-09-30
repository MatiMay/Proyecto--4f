import numpy as np
from stl import mesh

def calculate_normal(face):
    # Calculate the vectors for two edges of the face
    edge1 = face[1] - face[0]
    edge2 = face[2] - face[0]
    # Calculate the normal vector using the cross product
    normal = np.cross(edge1, edge2)
    # Normalize the normal vector
    normal = normal / np.linalg.norm(normal)
    return normal

def is_face_outward_facing(face, centroid):
    normal = calculate_normal(face)
    # Vector from centroid to a point on the face
    centroid_to_face = face[0] - centroid
    # Dot product to determine if the face is outward-facing
    dot_product = np.dot(normal, centroid_to_face)
    return dot_product > 0

def create_3d_object(coordinates):
    # Create the mesh
    obj_mesh = mesh.Mesh(np.zeros(len(coordinates), dtype=mesh.Mesh.dtype))
    for i, face in enumerate(coordinates):
        for j in range(3):
            obj_mesh.vectors[i][j] = face[j]
    
    # Calculate the centroid of the object
    centroid = np.mean(obj_mesh.vectors.reshape(-1, 3), axis=0)
    
    # Check each face
    for face in obj_mesh.vectors:
        if is_face_outward_facing(face, centroid):
            print("Face is outward-facing")
        else:
            print("Face is inward-facing")

# Example usage
coordinates = [
    np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0]]),
    np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]])
]
create_3d_object(coordinates)
