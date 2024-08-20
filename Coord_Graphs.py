import networkx as nx # type: ignore

import matplotlib.pyplot as plt # type: ignore

graphs = []
graph = nx.Graph()
graph3d = nx.Graph()

def Input_graphs():
    # Get the number of graphs from the user
    num_graphs = int(input("Enter the number of graphs: "))

    # Create a list to store the graphs

    # Create the graphs based on user input
    for i in range(num_graphs):
        nodes = input(f"Enter the nodes for graph {i+1} (separated by spaces): ").split()
        num_edges = int(input(f"Enter the number of edges for graph {i+1}: "))
        edges = []
        for _ in range(num_edges):
            edge = input(f"Enter an edge (format: node1 node2) for graph {i+1}: ").split()
            edges.append(edge)
        graph.add_edges_from(edges)
        graph.add_edges_from(edges)
        graphs.append(graph)


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

# Create the 3D graph
Input_graphs()
graph3d = create_3d_graph(graphs)
plot_3dGraf()

