import kruskalClass
import numpy as np
A = np.array([[0, 1, 4, 3],
                [0, 0, 0, 2],
                [0, 0, 0, 5],
                [0, 0, 0, 0]])

obj = kruskalClass.kruskalClass()

T = obj.findMinimumSpanningTree(A)
print(T)



