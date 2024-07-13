from functools import reduce
import math

listA = [3.0, 1.0, 7.2, 5.5]

def total_circle_area(list1):
    if(len(list1) == 0):
        return 0
    else:
        #return round(reduce(lambda x,y: x + y, (total_circle_areaHelper(list1))))
        return round(reduce(lambda x,y: x + y, (list(map(lambda x: math.pi*x**2, list1)))))
'''
def total_circle_areaHelper(list1):
    return list(map(lambda x: math.pi*x**2, list1))
'''    
sumA = total_circle_area(listA)

print(sumA)

print 'Its good to see you!'