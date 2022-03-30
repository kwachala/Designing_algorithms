import networkx as nx
import matplotlib.pyplot as plt
from random import uniform, randint, seed
from scipy.spatial import distance

N = 100
K = 100
D = 20
S = 21
R = 30

if N>=K:
    dl=N
else:
    dl=K

x=0
y=0
X = []
Y = []
XP = []
YP = []
tmp=0
maxlicz=0
licz=0
il=(N/D+1)**2
xtmp=0
ytmp=0

for m in range(int(il)):
    if m>0:
        xtmp=xtmp+20
        x = xtmp
    for n in range(int(il)):
        if n>0:
            ytmp=ytmp+20
            y=ytmp
        if licz>maxlicz:
            maxlicz=licz
            XP = X
            YP = Y
        X = []
        Y = []
        licz=0
        for i in range(int(dl/D)+1):
            for j in range(int(dl/D)+1):
                for l in range(len(X)):
                    s = distance.euclidean([X[l],Y[l]],[x,y])
                    if s >= S:
                        tmp = tmp + 1
                if tmp == len(X):
                    if y<=K and x<=N:
                        X.append(x)
                        Y.append(y)
                        licz=licz+1
                        print(licz)
                y = y + D
                tmp = 0
                if len(X) >= R:
                    break
            if len(X) >= R:
                break
            if x < N:
                x = x + D
            else:
                x = 0
            y=0

print(XP)
print(YP)

plt.scatter(XP, YP, label = 'Odwierty', color='g', marker = 'o')
plt.xlabel('N')
plt.ylabel('K')
plt.title('Nasz obszar')
plt.legend()
plt.axis([0,N,0,K])
plt.grid()
plt.show()
