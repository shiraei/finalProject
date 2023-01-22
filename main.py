import numpy as np
from numpy.linalg import eig
import networkx as nx
import random
from sklearn.preprocessing import normalize


#direct graph with dgree d:
d = 2
adjMatrix = np.zeros((d**4, d**4))
H = nx.DiGraph()
H.add_nodes_from(range(0, d**4))
for i in range(0, d**4):
    for j in range(0, d):
        x = random.randint(0, d**4-1)
        while H.has_edge(i, x) or x == i:
            x = random.randint(0, d ** 4 - 1)
        H.add_edge(i, x)
        adjMatrix[i][x] = 1
print(H.edges)
print(H.out_degree)
print(adjMatrix)


#normalize the adj matrix

adjNormed = normalize(adjMatrix, axis=1, norm='l1')
print(adjNormed)
#eigenvalue
w, v = eig(adjNormed)
print('E-value:', w)

#Absolute value
absV = [abs(ele) for ele in w]
print(absV)
print(max(absV))
absV.remove(max(absV))
print(absV)
print(max(absV))

#u = np.array([1, 2, 3])

#m = np.array([[2, 3, 4], [5, 6, 7], [1, 5, 8]])

#print(np.dot(u, m))
