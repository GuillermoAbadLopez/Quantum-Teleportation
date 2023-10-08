"""Helper functions file."""
import numpy as np
import networkx as nx
import pylab as plt


def random_state(nqubits: int):
    """Generates a random nqubit state vector.
    
    Args:
        nqubits (int): number of qubits of the state to generate.
    
    Returns:
        ndarray: Randomly generated nqubit states.
    """
    # Generate real and imaginary parts of the nqubit states.
    real_parts, im_parts = np.array([]), np.array([])
    for _ in range(2**nqubits):
        real_parts = np.append(real_parts, (np.random.random()*2)-1)
        im_parts = np.append(im_parts, (np.random.random()*2)-1)
    
    # Combine into list of complex numbers:
    amps = real_parts + 1j*im_parts
   
    # Normalise
    magnitude_squared = sum(abs(a)**2 for a in amps)
    return amps/np.sqrt(magnitude_squared)


def counts_of_one_register(counts: dict, register: int) -> dict:
    """Returns the counts of only one register, given the counts of various registers.
    
    Args:
        counts (dict): The counts of a results.
        register (int): The register from the passed one, that you want the counts from. The order is the one from the original counts.
        
    Returns:
        dict: The counts of the given register.
    """
    zeros, ones = 0, 0
    for state, count in counts.items():
        if state[2*register] == "0":
            zeros += count
        elif state[2*register] == "1":
            ones += count

    return {
        0: zeros,
        1: ones,
    }
    
    
def get_probabilities(counts: dict) -> dict:
    """Returns the counts as probabilities.
    
    Args:
        counts (dict): The counts of a results.
    
    Returns:
        dict: The probabilities associated to the given counts.
    """
    norm = sum(counts.values())
    return {i: count/norm for i, count in counts.items()}

def create_network_graph(edges: dict):
    """Create a networkx graph from a dicionary of edges.
    
    Args:
        edges (dict): The dicionary key is a tuple of the two nodes, and the value is the edge label.
    
    Returns:
        Displays the graph figure
    """
    G = nx.Graph()
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    labels = edges

    options = {"node_size": 1000, "node_color": "blue", "with_labels": True, "font_weight":'bold'}
    pos=nx.spring_layout(G)

    nx.draw(G, pos, **options)
    nx.draw_networkx_edge_labels(G, pos,edge_labels=labels,font_size=10)

    plt.show()
        