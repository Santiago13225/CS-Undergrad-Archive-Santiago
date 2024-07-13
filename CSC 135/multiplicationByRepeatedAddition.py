
# Multiplies a and non-negative b using repeated addition
def mult(a, b):
    if b == 0:
        #print('b: ' + str(b) + ', returned 0!')
        return 0
    else:
        #print('(*Before) a: ' + str(a) + ', b: ' + str(b) + ', (a+mult(a, b-1)): ' + str(a+mult(a, b-1)))
        #print('(*After) a: ' + str(a) + ', b-1: ' + str(b-1) + ', (a+mult(a, b-1)): ' + str(a+mult(a, b-1)))
        return a + mult(a, b-1)


# Multiplies a and non-negative b using repeated addition
# This one uses tail recursion!
def _mult2(a, b, acc):
    if b == 0:
        #print('b: ' + str(b) + ', returned acc!')
        return acc
    else:
        #print('(*Before) a: ' + str(a) + ', b: ' + str(b) + 'acc: ' + str(acc))
        #print('(*After) a: ' + str(a) + ', b-1: ' + str(b-1) + 'acc+a: ' + str(acc+a))
        return _mult2(a, b-1, acc+a)
             
def mult2(a,b):
    return _mult2(a, b, 0)

# Multiplies a and non-negative b using repeated addition
# This one uses tail recursion and a loop!
def mult3(a, b, acc=0):
    while True:
        if b == 0:
            #print('b: ' + str(b) + ', returned acc!')
            return acc
        else:
            #print('(*Before) a: ' + str(a) + ', b: ' + str(b) + ', acc: ' + str(acc))
            #print('(*After) a: ' + str(a) + ', b-1: ' + str(b-1) + ', acc+a: ' + str(acc+a))
            (a,b,acc) = (a, b-1, acc+a)
            
#def mult3(a,b):
    #return _mult3(a, b, 0)

print('Result: ' + str(mult3(2,5)))