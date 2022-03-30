import networkx as nx
import matplotlib.pyplot as plt
from random import uniform, randint, seed
from scipy.spatial import distance

x=10
g = nx.Graph()
gpos = {}
gr = nx.Graph()
grpos = {}

for i in range(x):
    x_rand = uniform(0, 5)
    y_rand = uniform(0, 5)
    g.add_node(i+1)    if i>0:
        g.add_edge(i,i+1)
    gpos[i+1] = [x_rand, y_rand]


nx.draw(g, gpos, with_labels=True, node_color="yellow")
plt.show()

def dist(v,w):
    gr.add_node(v)
    gr.add_node(w)
    grpos[v] = gpos[v]
    grpos[w] = gpos[w]

    if g.has_edge(v,w) == True:
        gr.add_edge(v, w)
        nx.draw(gr, grpos, with_labels=True, node_color="yellow")
        plt.show()
        return distance.euclidean(gpos[v], gpos[w])
    else:
        g.remove_node(v)
        if v == 1:
            S = [v+1]
            s = distance.euclidean(gpos[v], gpos[S[0]])
            gr.add_edge(v, S[0])
            return dist(S[0],w) + s
        elif v == x:
            S = [v-1]
            s = distance.euclidean(gpos[v], gpos[S[0]])
            gr.add_edge(S[0], v)
            return dist(S[0], w) + s
        else:
            S = [v-1, v+1]
            g.add_edge(S[0],S[1])
            if w>v:
                s = distance.euclidean(gpos[v], gpos[S[1]])
                gr.add_edge(v, S[1])
                return dist(S[1], w) + s
            else:
                s = distance.euclidean(gpos[v], gpos[S[0]])
                gr.add_edge(v, S[0])
                return dist(S[0], w) + s


print(dist(10,7))
