num_pop = -72

#count = 0

def count_digits(num):
    count = 0
    num = abs(num)
    while num != 0:
        num = num // 10
        count += 1
    return count
   
    #return count
return_value = count_digits(num_pop)

print('Number of digits: {}'.format(return_value))