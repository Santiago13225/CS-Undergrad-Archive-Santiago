
#This looks for the greatest common divisor (GCD) of two or more integers,
#which are not all zero, is the largest positive integer that divides each
#of the integers.
'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
'''
'''
# This one uses tail recursion!
def _gcd(a,b,acc):
    if acc==0:
        return acc
    else:
        #print('a: ' + a + 'a: ')
        return _gcd(a, b, a%b)
        
        
def gcd(a,b):
    return _gcd(a, b, 1)  # Initialize accumulator to something appropriate     

'''
def gcd(a,b):
    while True:
        if b==0:
            return a
        else:
            (a, b) = (b, a%b)

result = gcd(24,36)
print("GCD: " + str(result))