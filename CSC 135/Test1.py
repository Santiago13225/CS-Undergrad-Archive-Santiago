from functools import reduce
import math

listA = [3.0, 1.0, 7.2, 5.5]

def total_circle_area(list1):
    if(len(list1) == 0):
        return 0
    else:
        list2 = total_circle_areaHelper(list1)
        sum1 = reduce(lambda x,y: x + y, list2)
        sum2 = round(sum1)
        return sum2

def total_circle_areaHelper(list1):
    return list(map(lambda x: math.pi*x**2, list1))
    
sumA = total_circle_area(listA)

print(sumA)