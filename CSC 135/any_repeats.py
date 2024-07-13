t_list1 = ('red', 'blue', 'yellow', 'green', 'black', 'red')
t_list2 = ('boy')
t_list3 = ('red', 'blue', 'yellow', 'green', 'black')
t_list4 = ('red', 'blue', 'yellow', 'green', 'black', 'Red')

def any_repeats(tuple_list):#declares function with tuple parameter
    """
    If the tuple only has 1 or 0 elements, then it could
    not have a string that appears more than once in the
    tuple. So, it would be false by default.
    """
    if len(tuple_list) == 0 or len(tuple_list) == 1:
        return False
    
    else:
        #Creating a set from a list.
        a = []
        set_vals = set(a)
        #For each element in the tuple list, add the element to the set.
        for element in tuple_list:
            set_vals.add(element)
    """
    If length of the tuple is not equal to the length of the set, 
    then return true, as there is an element that appears more than
    once. Otherwise, return false!
    """
    return not(len(tuple_list) == len(set_vals))
    
return_value = any_repeats(t_list1)
print('{}'.format(return_value))