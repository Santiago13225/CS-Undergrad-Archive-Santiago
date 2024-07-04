
def fact(x):
    if x==0:
        #print('x: ' + str(x) + ', returned 1!')
        return 1
    else:
        #print('(*Before) x: ' + str(x) + ', fact(x-1): ' + str(fact(x-1)))
        #print('(*After) x * fact(x-1): ' + str(x * fact(x-1)))
        return x * fact(x-1)


# This one uses tail recursion!
def _fact2(x, acc):  # x! * acc is the answer to the original fact(x) call
    if x==0:
        #print('Returned acc: ' + str(acc))
        return acc
    else:
        # If x! * acc == y here...
        #print('(*Before) x: ' + str(x) + ', x-1: ' + str(x-1))
        #print('(*After) _fact2(x-1, acc * x): ' + str(_fact2(x-1, acc * x)))
        return _fact2(x-1, acc * x)
        # ...then it does here too.

def fact2(x):
    return _fact2(x, 1)  # Initialize accumulator to something appropriate


# This one uses tail recursion and a loop!
def _fact3(x, acc):  # x! * acc is the answer to the original fact(x) call
    while True:
        if x==0:
            #print('Returned acc: ' + str(acc))
            return acc
        else:
            #print('(*Before) x: ' + str(x) + ', x-1: ' + str(x-1) + ', acc: ' + str(acc))
            #print('(*After) (x-1, acc * x): ' + str((x-1, acc * x)))
            (x, acc) = (x-1, acc*x)

def fact3(x):
    return _fact3(x, 1)  # Initialize accumulator to something appropriate


#print('Factorial Result (1): ' + str(fact(3)))

#print('Factorial Result (2): ' + str(fact2(3)))

print('Factorial Result (3): ' + str(fact3(3)))