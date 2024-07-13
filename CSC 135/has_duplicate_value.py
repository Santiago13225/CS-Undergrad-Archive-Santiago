m = {'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Meghan': 'Miller', 'Hal': 'Perkins'}

def has_duplicate_value(dict1):
    
    if len(dict1) == 0 or len(dict1) == 1:
        return False
    
    else:
        a = []
        u_nums1 = set(a)
        
        for value in dict1.values():
            u_nums1.add(value)
        
        return len(dict1) != len(u_nums1)
    
    #return count
    
return_value = has_duplicate_value(m)
print('{}'.format(return_value))