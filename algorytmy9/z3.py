import sys
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

V = vertices
INF = sys.maxsize

def floydWarshall(dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    for i in range(V):
        for j in range(V):
            if dist[i][j] == sys.maxsize:
                dist[i][j] = 'I'
    return dist

# [4, 3, 1, 2, 0]

def printSolution(dist):
    for i in range(len(dist)):
        print(dist[i])

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

print(labels)
for i in range(V):
    for j in range(V):
        if matrix[i][j] == 0:
            matrix[i][j] = INF

for i in range(V):
    matrix[i][i] = 0

x = floydWarshall(matrix)
printSolution(x)

w1 = int(input('Podaj w1:'))
w2 = int(input('Podaj w2:'))
print(x[w1][w2])