def _fun_1_tail(n, acc):
    if(n == 1):
        return acc
    else:
        return _fun_1_tail(n//2, acc+1)

def fun_1_tail(n):
    return _fun_1_tail(n, 0)

def _fun_1_loop(n, acc=0):
    while True:
        if(n == 1):
            return acc
        else:
            (n, acc) = (n//2, acc+1)

def fun_1_loop(n, acc=0):
    return _fun_1_loop(n, 0)



# It calculates a*b (a multiplied b)
def fun_2(a, b):
    if (b == 0):
        return 0
    if (b % 2 == 0):
        return fun_2(a + a, b//2)
    return fun_2(a + a, b//2) + a

# It calculates a*b (a multiplied b)
def _fun_2_tail(a, b, acc):
    if (b == 0):
        return acc
    if (b % 2 == 0):
        return _fun_2_tail(a + a, b//2, acc)
    return _fun_2_tail(a + a, b//2, acc + a)

def fun_2_tail(a, b):
    return _fun_2_tail(a, b, 0)

# It calculates a*b (a multiplied b)
def _fun_2_loop(a, b, acc):
    while True:
        if (b == 0):
            return acc
        if (b % 2 == 0):
            (a,b,acc) = (a + a, b//2, acc)
        (a,b,acc) = (a + a, b//2, acc + a)

def fun_2_loop(a, b):
    return _fun_2_loop(a, b, 0)



print('Result: ' + str(fun_2_loop(3,6)))