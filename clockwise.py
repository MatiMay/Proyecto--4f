import numpy as np

def cross_product(v1, v2):
    return np.array([
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ])

def determine_orientation(p, q, r):
    # Convert points to numpy arrays
    p = np.array(p)
    q = np.array(q)
    r = np.array(r)
    
    # Compute edge vectors
    pq = q - p
    pr = r - p
    
    # Compute cross product
    normal = cross_product(pq, pr)
    
    # Check the z-component
    if normal[2] > 0:
        return "Counterclockwise (CCW)"
    elif normal[2] < 0:
        return "Clockwise (CW)"
    else:
        return "Collinear"

# Example usage
a = [0, 0, 0]
b = [0, 0, 1]
c = [0, 1, 0]
e = [1, 0, 0]

triangles = [
    [b, a, e],  # Triangle 1
    [e, c, b],  # Triangle 2
    [e, a, c],  # Triangle 3
    [b, c, a]   # Triangle 4
]

for i, triangle in enumerate(triangles, 1):
    orientation = determine_orientation(*triangle)
    print(f"Triangle {i}: {orientation}")
