def mergesort(a):
    # initialize inds array
    inds = [None]*len(a)

    # call private mergesort method
    __mergesort(a, inds)
    return a, inds

def __mergesort(a, inds):
    # base case:
    if len(a) <= 1: return 
    # recursive case:
    else: 
        # get mid point
        mid = (len(a) // 2) 

        # get upper half and lower half
        upper = a[mid:]
        lower = a[:mid]   

        # run mergesort on upper half and lower half
        __mergesort(upper, inds)
        __mergesort(lower, inds)

        # combining
        # define pointers
        u_point = l_point = index = 0 

        while(u_point < len(upper) and l_point < len(lower)):
            if upper[u_point] < lower[l_point]:
                a[index] = upper[u_point]
                inds[index] = u_point + len(lower)
                u_point += 1 
            elif upper[u_point] >= lower[l_point]:
               a[index] = lower[l_point]
               inds[index] = l_point
               l_point += 1
            index += 1 
        
        # if u_point exceeds upper array, add the rest of lower array to results
        while(l_point < len(lower)):
            a[index] = lower[l_point]
            inds[index] = l_point
            index += 1
            l_point += 1

        # if l_point exceeds lower array, add the rest of upper array to results
        while(u_point < len(upper)):
            a[index] = upper[u_point]
            inds[index] = u_point + len(lower)
            index += 1
            u_point += 1

    return a, inds

array = [5, 4, 3, 2, 1]

sorted, indices = mergesort(array)
print(sorted)
print(indices)
