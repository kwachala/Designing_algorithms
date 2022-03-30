import networkx as nx
import matplotlib.pyplot as plt

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


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        print(self.graph)

        while self.searching_algo_BFS(source, sink, parent):

            test = self.graph
            path_flow = float("Inf")
            s = sink

            pg = nx.DiGraph()

            for i in range(vertices):
                for j in range(vertices):
                    if self.graph[i][j] != 0:
                        pg.add_edge(i, j, weight=str(self.graph[i][j]) + '//' + str(test[j][i]))

            pos = nx.circular_layout(pg)
            nx.draw(pg, pos, with_labels=True)
            labels = nx.get_edge_attributes(pg, 'weight')
            nx.draw_networkx_edge_labels(pg, pos=nx.circular_layout(pg), edge_labels=labels)

            plt.show()

            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            print(self.graph)
            print(parent)

            pg = nx.DiGraph()

            for i in range(vertices):
                for j in range(vertices):
                    if self.graph[i][j] != 0:
                        pg.add_edge(i, j, weight=str(self.graph[i][j]) + '//' + str(test[j][i]))

            pos = nx.circular_layout(pg)
            nx.draw(pg, pos, with_labels=True)
            labels = nx.get_edge_attributes(pg, 'weight')
            nx.draw_networkx_edge_labels(pg, pos=nx.circular_layout(pg), edge_labels=labels)

            plt.show()

        return max_flow


pg = nx.DiGraph()

for i in range(vertices):
    for j in range(vertices):
        if matrix[i][j] != 0:
            pg.add_edge(i, j, weight=matrix[i][j])

pos = nx.circular_layout(pg)
nx.draw(pg, pos, with_labels=True)
labels = nx.get_edge_attributes(pg, 'weight')
nx.draw_networkx_edge_labels(pg, pos=nx.circular_layout(pg), edge_labels=labels)

plt.show()

g = Graph(matrix)

source = 0
sink = 5

print("Maksymalny przeplyw: %d " % g.ford_fulkerson(source, sink))
