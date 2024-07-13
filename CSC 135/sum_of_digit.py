# Recursive Python3 program to
# find sum of digits of a number

'''
# Function to check sum of digits using recursion
def sum_of_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10 + sum_of_digit(int(n / 10)))
'''
'''
# This one uses tail recursion!
def _sum_of_digit(n,acc):
    if n == 0:
        return acc
    else:
        return (_sum_of_digit(int(n / 10),(acc + n % 10)))
    
def sum_of_digit(n):
    return _sum_of_digit(n, 0)  # Initialize accumulator to something appropriate
'''
# This one uses tail recursion and a loop!
def _sum_of_digit(n,acc):
    while True:
        if n == 0:
            return acc
        else:
            (n, acc) = ((int(n / 10)),(acc + n % 10))
    
def sum_of_digit(n):
    return _sum_of_digit(n, 0)  # Initialize accumulator to something appropriate

print('Result: ' + str(sum_of_digit(268)))