class list135:
    
    def __init__(self, first_item = None, rest_of_list = None):
        self._first_item = first_item
        self._rest_of_list = rest_of_list
                
    def cons(self, first_item):
        return list135(first_item, self)
    
    def __str__(self):
        result = "["
        cur = self
        if cur._rest_of_list != None:
            result = result + str(cur._first_item)
            cur = cur._rest_of_list
        while cur._rest_of_list != None:
            result = result + "," + str(cur._first_item)
            cur = cur._rest_of_list
        return result + "]"
    
    def first(self):
        return self._first_item
    
    def rest(self):
        return self._rest_of_list
    
    def empty(self):
        return self._rest_of_list == None
    
    #Returns the number of elements in the list
    def len(self):
        if self._rest_of_list == None:
            return 0
        else:
            count = 0
            cur = self
            while cur._rest_of_list != None:
                count += 1
                cur = cur._rest_of_list
            return count
'''
    def count_true():
'''



'''
    def reverse(self):
        result2 = ""
        cur = self
        if cur._rest_of_list.empty():
            result2 = result2 + "[" + cur._first_item
            print(result2)
            return result2
        else:
            result2 = result2 + str(cur._rest_of_list.reverse()) + "," + str(cur._first_item)
            #if cur.len() == "4":
            print(result2)
                #result2 = result2 + "]"
            return result2
'''

# Write your tail-recursive version here following the pattern seen in class
'''
def _reverse(list_135_obj, acc):
    cur = list_135_obj #Set cur to list object.
    if(cur._rest_of_list == None): #If rest of list is empty.
        #acc = acc.cons(cur._first_item) #Add the only node.
        return acc #Return result of accumulator.
    else: #Acc works like the cons statements printed below.
        acc = acc.cons(cur._first_item) #This is like b = a.cons("B").
        cur = cur._rest_of_list #Move the "index" over one spot in the list object.
        return _reverse(cur, acc) #Return the new list object with the accumulator.
        
def reverse(list_135_obj):
    return _reverse(list_135_obj, list135()) #Return the result of the _reverse method.
'''

def _reverse(list_135_obj, acc):
    cur = list_135_obj #Set cur to list object.
    while True:
        if(cur._rest_of_list == None): #If rest of list is empty.
            #acc = acc.cons(cur._first_item) #Add the only node.
            return acc #Return result of accumulator.
        else: #Acc works like the cons statements printed below.
            acc = acc.cons(cur._first_item) #This is like b = a.cons("B").
            cur = cur._rest_of_list #Move the "index" over one spot in the list object.
            #_reverse(cur, acc) #Return the new list object with the accumulator.

def reverse(list_135_obj):
    return _reverse(list_135_obj, list135()) #Return the result of the _reverse method.
'''
'''
#a = list135("A")
#print(a)
#b = a.cons("B")
#print(b)
#c = a.cons("C")
#print(c)
#d = c.cons("D")
#print(d)
#e = d.rest()
#print(e)
#f = e.cons("F")
#print(f)    

#v0 = list135(12)
#print(v0)
#v1 = v0.cons(1)
#v2 = v1.cons(2)
#v3 = v2.cons(3)
#print(v0)
#print(v0.len())
#print(v1)
#print(v1.len())
#print(v2)
#print(v2.len())
#print(v3)
#print(v3.len())
    
t = list135()
#print(t)
a = t.cons("A")
#print(a)
b = a.cons("B")
#print(b)
c = b.cons("C")
#print(c)
d = c.cons("D")
print(d)

result = reverse(d)
print(result)
#e = d.rest()
#print(e)
#f = e.rest()
#print(f)
#g = f.rest()
#print(g)
#h = g.rest()
#print(h)
#i = h.rest()
#print(i)
#j = i.rest()
'''
print(v0.empty())
print(v1.empty())
print(v3.first())
print(v3.rest())
'''