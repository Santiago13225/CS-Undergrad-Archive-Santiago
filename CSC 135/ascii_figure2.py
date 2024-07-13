first = 1
second = 2
third = 3

def count_unique(int1, int2, int3):
    if(int1 == int2 and int2 == int3):
        return 1
    elif((int1 == int2 and int2 != int3) or (int2 == int3 and int1 != int2) or (int1 == int3 and int2 != int3)):
        return 2
    else:
        return 3

#return count
return_value = count_unique(first, second, third)

print('Numbers counted twice: {}'.format(return_value))