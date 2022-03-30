import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

N = 4


class Graph(object):

    def __init__(self, size, directed=False):
        s = (size, size)
        self.adjMatrix = np.zeros(s)
        self._directed = directed

    def add_edge(self, v1, v2):
        if self._directed == False:
            if v1 == v2:
                print("Same vertex %d and %d" % (v1, v2))
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1
        else:
            self.adjMatrix[v1][v2] = 1

    def print_matrix(self):
        print(self.adjMatrix)

    def give(self):
        return self.adjMatrix


def multiply(a, b, res):
    mul = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            mul[i][j] = 0
            for k in range(N):
                mul[i][j] += a[i][k] * b[k][j]

    for i in range(N):
        for j in range(N):
            res[i][j] = mul[i][j]


def power(G, res, n):
    if (n == 1):
        for i in range(N):
            for j in range(N):
                res[i][j] = G[i][j]
        return

    power(G, res, n // 2)
    multiply(G, G, res)

    if (n % 2 != 0):
        multiply(res, G, res)


if __name__ == '__main__':
    g = Graph(N)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    Gr = nx.DiGraph()
    Gr.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3)])

    pos = nx.spring_layout(Gr)
    nx.draw_networkx_nodes(Gr, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(Gr, pos)
    nx.draw_networkx_edges(Gr, pos, edge_color='r', arrows=True)

    plt.show()

    g.print_matrix()

    G = []
    u = g.give()

    for i in range(N):
        G.append(u[i])

    x = input('Podaj 1 wierzcholek:')
    y = input('Podaj 2 wierzcholek:')

    for k in range(1, N):
        res = np.zeros((N, N))
        power(G, res, k)
        print(res)
        print(res[int(x)][int(y)])
        if res[int(x)][int(y)] != 0:
            z = k
            break
        z = 'Nie ma takiej sciezki'

    if type(z) == int:
        print('Dla podanych wierzcholkow znaleziono dlugosc sciezki:')
        print(z)
    else:
        print(z)

    spojnosc = True
    for i in range(N):
        for j in range(N):
            if z == 0:
                spojnosc = False
            for k in range(1, N):
                z = 0
                res = np.zeros((N, N))
                power(G, res, k)
                z += res[int(i)][int(j)]
    if spojnosc == True:
        print('Graf jest spojny')
    else:
        print('Graf nie jest spojny')
