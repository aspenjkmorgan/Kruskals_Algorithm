# Creator: Aspen Morgan
# Last updated: 10/5/23

import numpy as np

class kruskalClass():

    def __init__(self):
        self = self

    # Input: ‘A’ is an NxN numpy array representing an adjacency matrix representation of a graph. If 𝐴𝑖𝑗=𝑤>0 it implies there is an edge between nodes 𝑖 and 𝑗 with weight 𝑤. We will only consider undirected graphs, and therefore ‘A’ will be an upper right triangular matrix. You can assume no two edge weights are the same.
    # Output: ‘T‘ is an NxN numpy array representing the minimum spanning tree of
    # ‘A’. We will only consider undirected graphs, and therefore ‘T’ should be an
    # upper right triangular matrix.
    def findMinimumSpanningTree(self, A):
        # convert to 1xK array
        N = len(A)
        B = []
        for i in range(0, N):
            for j in A[i]:
                B.append(j)

        # sort all edges in ascending order
        B, indices = self.mergesort(B)

        # create union-find object with n nodes
        u = self.makeUnionFind(N)

        # initialize the empty tree with all zeros
        T = np.zeros((N, N))

        # consider edge weights in ascending order, ignore zeros
        # for each edge, if its nodes aren't connected: add to tree and update union find
        # continue adding until there are N-1 edges in tree
        edges_count = x = 0
        while(edges_count < N - 1):
            if B[x] != 0:
                # get the associated nodes: v=row and w=col
                index = indices[x]
                v = index // N
                w = index % N

                # if they are not already conncected, 
                # add the edge to the tree in the right spot
                # and union the nodes
                if self.find(u, v) != self.find(u, w):
                    T[v, w] = B[x]
                    edges_count += 1
                    self.union(u, v, w)
            
            x += 1
        
        return T

    # Input: ‘a’ must be a 1xK numpy array.
    # Output: ‘b’ must be a 1xK numpy array with elements in ascending order (i.e.,
    # lowest value to highest). ‘inds’ must be a 1xK numpy array with the index in ‘a’ of
    # each entry in the sorted output array ‘b’.
    def mergesort(self, a):
        # initialize inds array, zeros index array, and auxillary array
        aux = []
        inds = []
        zeros = []
        zeros_inds = []

        # since weights are unique besides 0s, a hash table can store them
        # put all zeros in beginning
        dict = {}
        for i in range(0, len(a)):
            if a[i] == 0:
                zeros_inds.append(i)
                zeros.append(0)
            else:
                dict[a[i]] = i
                aux.append(a[i])
        
        self.__mergesort(aux)

        # use b and dictionary to get rest of indices 
        for k in range(0, len(aux)):
            inds.append(dict[aux[k]])

        # combine arrays for zeros with the rest
        inds = zeros_inds + inds
        aux =  zeros + aux

        return aux, inds
    
    def __mergesort(self, array):
        # base case:
        if len(array) <= 1: return array
        # induction step:
        else: 
            # get mid point
            mid = (len(array) // 2) 

            # get upper half and lower half
            upper = array[mid:]
            lower = array[:mid]   

            # run mergesort on upper half and lower half
            self.__mergesort(upper)
            self.__mergesort(lower)

            # combining step:
            # define pointers
            u_point = l_point = index = 0 

            while(u_point < len(upper) and l_point < len(lower)):
                if upper[u_point] < lower[l_point]:
                    array[index] = upper[u_point]
                    u_point += 1 
                elif upper[u_point] >= lower[l_point]:
                    array[index] = lower[l_point]
                    l_point += 1
                index += 1 
                
            # if u_point exceeds upper array, add the rest of lower array to results
            while(l_point < len(lower)):
                array[index] = lower[l_point]
                index += 1
                l_point += 1

            # if l_point exceeds lower array, add the rest of upper array to results
            while(u_point < len(upper)):
                array[index] = upper[u_point]
                index += 1
                u_point += 1
        return array

    # Input: ‘N’ is the number of nodes in a graph.
    # Output: ‘u’ is a 1XN python dictionary, where the keys are numerical labels for
    # the nodes, and the values are numpy arrays with the 0th entry being a pointer to a
    # node in the same dictionary. The numpy arrays can be more than one 1-D if you
    # want, but they must be numpy arrays, and the 0th entry must contain pointers to
    # other nodes that are used in the ‘find’ and ‘union’ functions.
    def makeUnionFind(self, N):
        # We will always have at least one element
        u = {0: np.array([0])}
        for i in range(0, N):
            u.update({i: np.array([i])})
        return u

    # Input: ‘u’ is a union-find data structure. ‘v’ is a numerical index for a graph node.
    # Output: ‘s’ is the numerical value corresponding to the label for the set of
    # connected nodes to which ‘v’ belongs.
    def find(self, u, v):
        old_v_values = []
        while v != u[v][0]:
            # add old v value to list for path compression
            old_v_values.append(v)
            v = u[v][0]
        
        # compress path for these nodes
        for edge in old_v_values:
            u.update({edge: np.array([v])})

        return v

    # Input: ‘u_in’ is a union-find data structure. ‘s1’ and ‘s2’ are numerical values
    # corresponding to the labels of two groups of graph nodes.
    # Output: ‘u_out’ is the same as ‘u-in’, except that the two groups of nodes, ‘s1’
    # and ‘s2’, have been merged into a single group with a single label.
    def union(self, u_in, s1, s2):
        # get root of subset 1
        root1 = self.find(u_in, s1)

        # point node 2 to the subset 1 root
        u_in.update({s2: np.array([root1])})

        return u_in