l1 = [1, 4, 2, 4, 7, 1, 1, 9, 2, 3, 4, 1]

def count_duplicates(list1):
    
    if len(list1) == 0 or len(list1) == 1:
        return 0
    
    index = 0
    count = 0
    d_count = 0
    
    while index < len(list1):
        count = index + 1
        while count < len(list1):
            if list1[index] == list1[count]:
                d_count += 1
                break
            
            count += 1

        index +=1
        
    return d_count
    
return_value = count_duplicates(l1)
print('{}'.format(return_value))