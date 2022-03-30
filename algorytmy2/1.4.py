import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random

def plot_matrix(rm, title='', cmap=plt.cm.Blues):
    plt.imshow(rm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.tight_layout()
    plt.show()

def nb_list(matrix, i,j):
    x = matrix.shape[0]-1
    y= matrix.shape[1]-1
    if i != x and j != y:
        nb = [matrix[i+1][j], matrix[i-1][j], matrix[i][j+1], matrix[i][j-1]]
    elif i == x and j != y:
        nb = [matrix[i - 1][j], matrix[i][j + 1], matrix[i][j - 1]]
    elif i != x and j == y:
        nb = [matrix[i + 1][j], matrix[i - 1][j], matrix[i][j - 1]]
    else:
        nb = [matrix[i - 1][j], matrix[i][j - 1]]
    return nb

cmap = colors.ListedColormap(['k','b','y','g','r'], N= 5)
#cmap = colors.ListedColormap(['b','g','r'], N= 3)
rm = np.zeros((5,5))

for i in range(0, 5):
    for j in range(0,5):
        seq = [1, 2, 3, 4, 5]
        #seq = [1, 2, 3]
        k = random.choice(seq)
        if k in nb_list(rm, i, j):
            while k in nb_list(rm, i, j):
                seq.remove(k)
                k = random.choice(seq)
        rm[i][j] = k
print(rm)
plot_matrix(rm,cmap=cmap)