import math
# convert the following with Tail Recursion and Loop varients

#################################
# A NON-TAIL-RECURSIVE FUNCTION #
#################################
def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

# The function calculates and returns log_2(n)
# Assume that n is greater than or equal to 1
# if n is between 8 and 15 then returns 3
# If n is between 16 to 31 then returns 4
def fun_1(n):
    if(n == 1):
        return 0
    else:
        return 1 + fun_1(n//2)

# It calculates a*b (a multiplied b)
def fun_2(a, b):
    if (b == 0):
        return 0
    if (b % 2 == 0):
        return fun_2(a + a, b//2)
    return fun_2(a + a, b//2) + a
        
##########################
# TAIL-RECURSIVE VERSION #
##########################

def fact_tail(n):
    pass

def fun_1_tail(n):
    pass

def fun_2_tail(n):
    pass

################
# LOOP VERSION #
################

def fact_loop(n):
    pass

def fun_1_loop(n):
    pass

def fun_2_loop(n):
    pass

# Factorial
assert math.factorial(int(5)) == fact(5), "fact NON-tail-recursive"
assert math.factorial(int(5)) == fact_tail(5), "fact tail-recursive"
assert math.factorial(int(5)) == fact_loop(5), "fact loop: Expected"
print("\n\n")

# The function calculates and returns log_2(n)
assert 3 == fun_1(15), "fun_1 NON-tail-recursive"
assert 3 == fun_1_tail(15), "fun_1 tail-recursive"
assert 3 == fun_1_loop(15), "fun_1 loop"
print("\n\n")

assert 4 == fun_1(16), "fun_1 NON-tail-recursive"
assert 4 == fun_1_tail(16), "fun_1 tail-recursive"
assert 4 == fun_1_loop(16), "fun_1 loop"
print("\n\n")

assert 4 == fun_1(2,2), "fun_1 NON-tail-recursive"
assert 8 == fun_1_tail(2,4), "fun_1 tail-recursive"
assert 16 == fun_1_loop(2,8), "fun_1 loop"
print("\n\n")
