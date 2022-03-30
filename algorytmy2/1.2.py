import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import randint

def dist(v1, v2):
    distance = ((Vx[v1] - Vx[v2])**2 + (Vy[v1] - Vy[v2])**2)**0.5
    return distance

V = [1, 2, 3, 4, 5]
W = []
Vx = {}
Vy = {}

#losowanie pozycji (vx, vy)
for v in V:
    Vx[v] = randint(0, 100)
    Vy[v] = randint(0, 100)
Vx = {1: 60, 2: 17, 3: 90, 4: 34, 5: 17}
Vy = {1: 76, 2: 99, 3: 9, 4: 56, 5: 85}

#tworzenie grafu
G = nx.Graph()
gpos = {}
for v in V:
    G.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]
for w in W:
    G.add_edge(w[0], w[1])


nx.draw(G, gpos, with_labels=True, node_color = 'yellow')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, gpos, edge_labels=labels)
plt.show()

edges = G.edges
for v in G.nodes:
    set = None
    min_dist = 100*1.5
    for w in G.nodes:
        if ((w, 1) in G.edges) or ((1, w) in G.edges) or (w == 1): #jest juz połaczony z v1 jakakolwiek sciezka (w szczególnosci moze to byc sciezka trywialna, czyli w = v1).
            if dist(v, w) < min_dist:
                min_dist = dist(v, w)
                set = (v, w)

    if set != None:
        G.add_edge(v, w)
        nx.draw(G, gpos, with_labels=True, node_color='yellow')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, gpos, edge_labels=labels)
        plt.show(block= False)
        plt.pause(2)
        plt.close()

print(Vx, Vy)