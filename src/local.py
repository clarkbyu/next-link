''' Next Link - Clark Brown - 2019

Local Methods for Link Prediction:
 - A local method is an algorithm that uses vertex neighborhoods to compute similarity between nodes
'''

import networkx as nx
import utils as u
import math

def common_neighbors(G):
    pass

def common_neighbors_score(G, x, y):
    ''' Common Neighbors
    Computes score(x,y) = |Γ(x) ∩ Γ(y)|, where Γ(x) is the neighbor set for x ∊ V.

    Parameters:
        G (graph): the graph that includes x and y
        x, y (node): the nodes to compute the score for

    Returns:
        score (int): the number of common neighbors
    '''
    score = len(sorted(nx.common_neighbors(G, x, y)))
    return 

def jaccard(G):
    pass

def jaccard_score(G, x, y):
    ''' Jaccard's Coefficient
    Computes score(x,y) = |Γ(x) ∩ Γ(y)|/|Γ(x) ∪ Γ(y)|, where Γ(x) is the neighbor set for x ∊ V.

    Parameters:
        G (graph): the graph that includes x and y
        x, y (node): the nodes to compute the score for

    Returns:
        score (int): the Jaccard Coefficient
    '''
    num = len(sorted(nx.common_neighbors(G, x, y)))

    x_neighbors = nx.neighbors(G, x)
    y_neighbors = nx.neighbors(G, y)

    if((len(x_neighbors) == 0) or (len(y_neighbors == 0))):
        return 0

    denom = len(u.union(x_neighbors, y_neighbors))

    score = num / denom
    return score

def preferential_attachment(G):
    pass

def preferential_attachment_score(G, x, y):
    ''' Preferential Attachment
    Computes score(x,y) = |Γ(x)||Γ(y)|, where Γ(x) is the neighbor set for x ∊ V.

    Parameters:
        G (graph): the graph that includes x and y
        x, y (node): the nodes to compute the score for

    Returns:
        score (int): the "connectedness" of the two nodes
    '''
    x_neighbors = nx.neighbors(G, x)
    y_neighbors = nx.neighbors(G, y)

    score = len(x_neighbors) * len(y_neighbors)

    return score

def adamic_adar(G):
    pass

def adamic_adar_score(G, x, y):
    ''' Adamic-Adar
    Computes score(x,y) = Σ (1/log(|Γ(y)|)) for z ∊ (Γ(x) ∩ Γ(y)), where Γ(x) is the neighbor set for x ∊ V.

    Parameters:
        G (graph): the graph that includes x and y
        x, y (node): the nodes to compute the score for

    Returns:
        score (int): the Adamic-Adar score for x and y
    '''
    score = 0

    for z in nx.common_neighbors(G, x, y):
        z_neighbors = len(nx.neighbors(G, z))
        score += (1 / math.log(z_neighbors))

    return score

def resource_allocation(G):
    pass

def resource_allocation_score(G, x, y):
    ''' Resource Allocation
    Computes score(x,y) = Σ (1/(|Γ(y)|)) for z ∊ (Γ(x) ∩ Γ(y)), where Γ(x) is the neighbor set for x ∊ V.

    Parameters:
        G (graph): the graph that includes x and y
        x, y (node): the nodes to compute the score for

    Returns:
        score (int): the Resource Allocation score for x and y
    '''
    score = 0

    for z in nx.common_neighbors(G, x, y):
        z_neighbors = len(nx.neighbors(G, z))
        score += (1 / z_neighbors)

    return score