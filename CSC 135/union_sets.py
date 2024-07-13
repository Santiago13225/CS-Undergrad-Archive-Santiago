super_set = {{1, 3}, {2, 3, 4, 5}, {3, 5, 6, 7}, {42}}



def union_sets(set_of_sets):
    
    frozen_item = frozenset(set_of_sets)
    
    
    a = set(set_of_sets)
    
    b = []
    high_set = set(b)
    
    for each_set in a:
        high_set.add(frozen_item)

    return high_set
   
    #return count
return_value = union_sets(a)

print('Number of common numbers: {}'.format(return_value))