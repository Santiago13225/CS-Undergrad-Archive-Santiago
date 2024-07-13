'''
def fibonacci(n, second_last, last):
    if n-1 == 0:
        return second_last
    else:
        new_last = second_last + last #a+b
        second_last = last #a<-b
        return fibonacci(n-1, second_last, new_last)
'''
# This one uses tail recursion!
def _fibonacci(n, second_last, last, acc=0):
    if n-1 == 0:
        return acc
    else:
        new_last = second_last + last #a+b
        second_last = last #a<-b
        return _fibonacci(n-1, second_last, last, acc + new_last+second_last)
       
#def fibonacci(n, sl, l):
#    return _fibonacci(n, sl, l, 0)  # Initialize accumulator to something appropriate
     

print('Result: ' + str(fibonacci(10,0,1)))