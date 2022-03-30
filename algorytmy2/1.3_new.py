import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance


def one(n, V):
    G = nx.Graph()
    pos = {}
    seed(2)
    for v in V:
        G.add_node(v)
        pos[v] = [randint(0, 100)*random(), randint(0, 100)*random()]
    #G = nx.complete_graph(G)
    for v in V:
        euclidian_distances = {}
        for vv in V:
            if vv == v:
                continue
            euclidian_distances[vv] = distance.euclidean(pos[v], pos[vv])
        minimum_distance = min(euclidian_distances,
                               key=euclidian_distances.get)
        G.add_edge(v, minimum_distance, weight=round(
            euclidian_distances[minimum_distance], 2))

    nx.draw(G, pos, with_labels=True, node_color='yellow')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    def dist(source, target):
        travel = nx.shortest_path(G, source=source, target=target)
        print(f'Travel from {source} to {target} is {travel}')
        dis = 0
        for i in range(len(travel)-1):
            dis = dis + distance.euclidean(pos[travel[i]], pos[travel[i+1]])
        print(f'Distance between {source} and {target} is {dis}')
    dist(58, 12)


n = 100
V = []
for i in range(n):
    V.append(i+1)
one(n, V)
