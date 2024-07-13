v = [1, 3, 1, 4, 3, 7, -2, 0, 7, -2, -2, 1]

def twice(list):
    
    a = []
    once = set(a)
    
    b = []
    twice = set(b)
    
    c = []
    more = set(c)
    
    for num in list:
        if num in once:
            once.remove(num)
            twice.add(num)
        elif num in twice:
            twice.remove(num)
            more.add(num)
        elif not(num in more):
            once.add(num)
            
    return twice

#return count
return_value = twice(v)

print('Numbers counted twice: {}'.format(return_value))