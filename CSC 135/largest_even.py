from functools import reduce

listA = [5, -1, 12, 10, 2, 8]
listB = [42]

def largest_even(list1):
    '''
    if(len(list1) == 1):
        return list1[0]
    else:
    '''
    #return largest_evenHelper2(list(filter(largest_evenHelper, list1)))
    return reduce(lambda x,y: x if x > y else y, (list(filter(largest_evenHelper, list1))))

def largest_evenHelper(list1):
    if (list1 % 2 == 0):
        return True
    else: 
        return False
'''
def largest_evenHelper2(list1):
    largestEven = reduce(lambda x,y: x if x > y else y, list1)
    return largestEven
'''
print(largest_even(listA))
print(largest_even(listB))