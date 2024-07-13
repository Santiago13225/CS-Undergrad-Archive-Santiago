grades = {"Hermione": 4, "Harry": 3.4, "Ron": 3.4, "Ginny": 3.8, "Draco": 3.7}

def deans_list(dict1):
    
    a = []
    smart_ones = set(a)
    
    if len(dict1) == 0:
        return smart_ones
    
    else:
        
        for key, value in dict1.items():
            if value >= 3.5:
                smart_ones.add(key)
        
        return smart_ones
    
    #return count
    
return_value = deans_list(grades)
print('{}'.format(return_value))