import networkx as nx
import matplotlib.pyplot as plt


x=10                             #liczba wierzcholkow

g = nx.Graph()
for i in range(1, x):
    g.add_edge(str(i), str(i+1))
g = nx.complete_graph(g)
gpos=nx.circular_layout(g)

nx.draw(g, gpos, with_labels=True, node_color="yellow")
plt.show()