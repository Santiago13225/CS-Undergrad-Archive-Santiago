l1 = [7, 2, 8, 9, 4, 13, 7, 1, 9, 10]
l2 = [1, 2, 3, 4, 5]
l3 = [100, -100]
l4 = [1, 2, 3]
l5 = [1]
l6 = []

def collapse(list1):
    
    if len(list1) == 0 or len(list1) == 1:
        return list1
    
    else:
        list2 = []
        index = 0

        print('{}'.format(list1))
        print('{}'.format(list2))
    
        for j in range(0, (len(list1)-1), 2):
            list2.append(list1[j] + list1[j + 1])
            index += 1
            print('{}'.format(list2))
        
        if index != (len(list1)+1)//2:
            list2.append(list1[len(list1) - 1])
        
    return list2   
   
    #return count
return_value = collapse(l1)
print('{}'.format(return_value))

return_value = collapse(l2)
print('{}'.format(return_value))

return_value = collapse(l3)
print('{}'.format(return_value))

return_value = collapse(l4)
print('{}'.format(return_value))

return_value = collapse(l5)
print('{}'.format(return_value))

return_value = collapse(l6)
print('{}'.format(return_value))