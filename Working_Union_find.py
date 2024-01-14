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