import numpy as np

N = 100


class Graph(object):

    def __init__(self, size, directed=False):
        s = (size, size)
        self.incMatrix = np.zeros(s)
        self._directed = directed
        self.highest = 0
        self.counter = 0

    def add_edge(self, v1, v2):

        if self._directed == False:
            if v1 == v2:
                print("Same vertex %d and %d" % (v1, v2))
            self.incMatrix[v1][self.counter] = 1
            self.incMatrix[v2][self.counter] = 1
        else:
            self.incMatrix[v1][self.counter] = 1
            self.incMatrix[v2][self.counter] = -1

        if v1 > self.highest:
            self.highest = v1
        if v2 > self.highest:
            self.highest = v2

        self.counter += 1

    def print_matrix(self):
        print(self.incMatrix)

    def give(self):
        return self.incMatrix

    def give_highest(self):
        return self.highest

    def give_counter(self):
        return self.counter

    def copy_matrix(self, sizee):
        self.cop = np.zeros(sizee)
        for i in range(sizee[0]):
            for j in range(sizee[1]):
                self.cop[i][j] = self.incMatrix[i][j]
        return self.cop


if __name__ == '__main__':
    g = Graph(N, directed=True)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)


    rows = g.give_highest() + 1
    columns = g.give_counter()

    size = (rows, columns)

    real_incMatrix = g.copy_matrix(size)
    print(real_incMatrix)