import sys
import networkx as nx
import matplotlib.pyplot as plt


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Najkrotsza sciezka od podanego wierzcholka do danych wierzcholkow:")
        for node in range(self.V):
            print('Wierzcholek:', node, "Dystans:", dist[node])

    def minDistance(self, dist, sptSet):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                print('min', min)
                min_index = v
                print('ind', min_index)

        return min_index

    def dijkstra(self, src, src2):
        prev = [0] * self.V

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            print(dist)
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    prev[v] = u

        path = [src2]

        path.append(prev[src2])
        i = 1
        while path[-1] != src:
            path.append(prev[path[i]])
            i += 1

        self.printSolution(dist)
        print('Odleglosc od', src, 'do', src2, 'wynosi', dist[src2])
        print('Sciezka:', path)


vertices = open('vertices.txt', 'r').read()
vertices = int(vertices)

get_matrix = open('matrix.txt', 'r')

matrix = []

for line in get_matrix:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    matrix.append(line_list)

get_matrix.close()

for i in range(vertices):
    for j in range(vertices):
        matrix[i][j] = int(matrix[i][j])


g = Graph(vertices)
g.graph = matrix

g.dijkstra(0, 4)

pg = nx.Graph()

for i in range(vertices):
    for j in range(vertices):
        if matrix[i][j] != 0:
            pg.add_edge(i, j, weight=matrix[i][j])

pos = nx.circular_layout(pg)
nx.draw(pg, pos, with_labels=True)
labels = nx.get_edge_attributes(pg, 'weight')
nx.draw_networkx_edge_labels(pg, pos=nx.circular_layout(pg), edge_labels=labels)

plt.show()
