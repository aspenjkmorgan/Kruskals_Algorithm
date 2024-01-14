def mergesort(a):
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
    
    __mergesort_helper(aux)

    # use b and dictionary to get rest of indices 
    for k in range(0, len(aux)):
       inds.append(dict[aux[k]])

    # combine arrays for zeros with the rest
    inds = zeros_inds + inds
    aux =  zeros + aux

    return aux, inds

def __mergesort_helper(a):
    # base case:
    if len(a) <= 1: return a 
    # induction step:
    else: 
        # get mid point
        mid = (len(a) // 2) 

        # get upper half and lower half
        upper = a[mid:]
        lower = a[:mid]   

        # run mergesort on upper half and lower half
        __mergesort_helper(upper)
        __mergesort_helper(lower)

        # combining step:
        # define pointers
        u_point = l_point = index = 0 

        while(u_point < len(upper) and l_point < len(lower)):
            if upper[u_point] < lower[l_point]:
                a[index] = upper[u_point]
                u_point += 1 
            elif upper[u_point] >= lower[l_point]:
               a[index] = lower[l_point]
               l_point += 1
            index += 1 
        
        # if u_point exceeds upper array, add the rest of lower array to results
        while(l_point < len(lower)):
            a[index] = lower[l_point]
            index += 1
            l_point += 1

        # if l_point exceeds lower array, add the rest of upper array to results
        while(u_point < len(upper)):
            a[index] = upper[u_point]
            index += 1
            u_point += 1

    return a

array = [0, 8, 0, 3, 0, 0, 2, 5, 0, 0, 0, 6, 0, 0, 0, 0]

sorted, indices = mergesort(array)
print(sorted)
print(indices)
