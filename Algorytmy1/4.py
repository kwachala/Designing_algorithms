import networkx as nx
import matplotlib.pyplot as plt
from random import uniform, randint

x=50                   #liczba wierzcholkow
g = nx.Graph()
gpos = {}
tmp = []
z = 0
licz = 0
fail = 0

while licz < x:
    x_rand = uniform(-5,5)
    y_rand = uniform(-5,5)
    for j in range(len(tmp)):
        if tmp[j] != [x_rand, y_rand]:
            z = z+1

    if len(tmp) == z:
        g.add_node(licz)
        gpos[licz] = [x_rand, y_rand]
        fail = 0
        print("git")
        label=1
        #if licz+1 < x:
        #    g.add_weighted_edges_from([(licz, licz+1, label)])
        licz = licz + 1

    else:
        fail = fail + 1
        print(fail)

    z=0
    tmp.append([x_rand, y_rand])

    if fail == 100:
        break

nx.draw(g, gpos, with_labels=True, node_color="yellow")
plt.show()