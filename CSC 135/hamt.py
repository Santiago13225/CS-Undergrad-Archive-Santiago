# Hash Array Mapped Trie - Used in CSC 135, Sacramento State
# Written by Ted Krovetz, February 2022
# 
# This implementation assumes that the objects pointed at by the key and value
# references stored in the HAMT structure do not change during the lifetime
# of the structure.
class hamt:
    
    DEG = 4      # Children per node (must be power of 2)
    BITS = 2     # log2(DEG), bits needed to select child
    MASK = 0b11  # Bitmask for extracting low BITS bits (DEG - 1)
    
    def __init__(self, key, value, children=None):
        self._key = key
        self._value = value
        if children == None:
            self._children = [None] * hamt.DEG
        else:
            self._children = children
    '''
    def _set(self, key, value, hashbits):
        # Each node encountered during search will get altered.
        # To maintain persistence, each is duplicated, updated, returned.
        if (self._key == key):
            # This node matches key. Return duplicate with new value
            print('hamt(self._key, value, self._children):')
            return hamt(self._key, value, self._children)
        else:
            # Continue search using hashbits to pick direction
            print('child_num = hashbits & hamt.MASK:')
            child_num = hashbits & hamt.MASK
            # Copy can reuse key/value. Child list gets updated, so duplicate
            print('copy = hamt(self._key, self._value, list(self._children)):')
            copy = hamt(self._key, self._value, list(self._children))
            if (copy._children[child_num] == None):
                print('if (copy._children[child_num] == None):')
                print('copy._children[child_num] = hamt(key, value):')
                # End of search, key not found, add new node
                copy._children[child_num] = hamt(key, value)
            else:
                # Continue by asking appropriate child to set key/value
                print('else:')
                print('copy._children[child_num] = copy._children[child_num]._set(key, value, hashbits >> hamt.BITS)')
                copy._children[child_num] = copy._children[child_num].     \
                                    _set(key, value, hashbits >> hamt.BITS)
            return copy  
        '''
    
    
    def _set(self, key, value, hashbits):
        # Each node encountered during search will get altered.
        # To maintain persistence, each is duplicated, updated, returned.
        if (self._key == key):
            # This node matches key. Return duplicate with new value
            return hamt(self._key, value, self._children)
        else:
            # Continue search using hashbits to pick direction
            child_num = hashbits & hamt.MASK
            
            # Copy can reuse key/value. Child list gets updated, so duplicate
            copy = hamt(self._key, self._value, list(self._children))
            
            if (copy._children[child_num] == None):
                # End of search, key not found, add new node
                copy._children[child_num] = hamt(key, value)
            else:
                # Continue by asking appropriate child to set key/values
                copy._children[child_num] = copy._children[child_num].     \
                                    _set(key, value, hashbits >> hamt.BITS)
            return copy  
    
    '''
    def _get_01(self, key, hashbits):
        if(self._key == key):
            return self._value
        else:
            child_num = hashbits & hamt.MASK
            if self._children[child_num] is not None:
                return self._children[child_num]._get(key, hashbits >> hamt.BITS)
            else:
                return None
    '''
    def _get(self, key, hashbits):
        child_num = hashbits & hamt.MASK
        if(self._key == key):
            return self._value
        elif (self._children[child_num] is not None):
            return self._children[child_num]._get(key, hashbits >> hamt.BITS)
        else:
            return None
    
    def set(self, key, value):
        # Pass key/value and hashbits to recursive helper
        return self._set(key, value, hash(key))
    
    def __str__(self):
        s = "[({},{})".format(str(self._key),str(self._value))
        for i in range(hamt.DEG):
            if (self._children[i] == None):
                s = s + "X"
            else:
                s = s + str(self._children[i])
        return s + "]"
    def map(self, func):
        copy = hamt(self._key, self._value, list(self._children))#First, we copy the tree.
        #if(copy._key is not None):#If the root node exists (*Also works as a sort of base case).
        #copy._value = func(copy._key, copy._value)#Set the root node's value with the function.
        for i in range(hamt.DEG):#For each possible path.
            if(copy._children[i] is not None):#If the child of the node exists.
                copy._children[i] = copy._children[i].map(func)#Then, we call the map function on the child recursively.
        copy._value = func(copy._key, copy._value)#Set the root node's value with the function.
        return copy#Return the duplicated trie with the new values.
    
    
    
    def map(self, func):
        copy = hamt(self._key, self._value, list(self._children))
        if(copy._key is not None):
            #self._value = func(copy._key, copy._value)
            copy._value = func(copy._key, copy._value)
        for i in range(hamt.DEG):
            '''
            if(copy._children[i] is None):
                print("Do nothing!")
            else:
                #self._children[i]._value = func(copy._children[i]._key, copy._children[i]._value)
                #copy._children[i]._value = func(copy._children[i]._key, copy._children[i]._value)
                copy._children[i].map(func(copy._children[i]._key, copy._children[i]._value))
                #map(self._children[i], func)
            #if(self._children[i] is not None):
            '''
            #print(copy._children[i])
            if(copy._children[i] is not None):
                #copy._value = func(copy._key, copy._value)
                #self._children[i]._value = func(copy._children[i]._key, copy._children[i]._value)
                #copy._children[i]._value = func(copy._children[i]._key, copy._children[i]._value)
                #copy._children[i].map(func)
                copy._children[i] = copy._children[i].map(func)
                #map(self._children[i], func)
            
        return copy
    #print(f.map(lambda k, v: k + v))
    '''
    def map(self, func):
        if (self._key is None):
            print('self._key is None!')
        else:
            new_trie = hamt(self._key, self._value.func(), list(self._children))
            for i in range(hamt.DEG):
                if(copy._children[i]._key is not None):
                    return hamt(self._key, func, self._children)
            # End of search, key not found, add new node
    
            
    
    def map(self, func):
        # Pass key/value and hashbits to recursive helper
        return self._map(func)
    #print(f.map(lambda k, v: str(k) + str(v)))
    def _map(self, func):
        # Each node encountered during search will get altered.
        # To maintain persistence, each node is duplicated, updated, returned.
        if (self._key is None):
            # This node is not none. Return duplicate with new value.
            print('if (self._key is None):')
            return hamt(self._key, self._value, self._children)
        else:
            copy = hamt(self._key, self._value, list(self._children))
            # Continue search using hashbits to pick direction.
            # Copy can reuse key/value. Child list gets updated, so duplicate
            for i in range(hamt.DEG):
                print('for i in range(hamt.DEG):')
                #copy = hamt(self._key, self._value, list(self._children))
    
                if (copy._children[i] is not None):
                    print('if (copy._children[child_num] is not None):')
                # Continue by asking appropriate child to set key/value
                    copy._children[i] = copy._children[i].     \
                                    _map(func)
                
    
                    copy._children[i] = copy._children[child_num[i]].     \
                                    _map(func)


            return copy
        
     def map(self, func):
        # Each node encountered during search will get altered.
        # To maintain persistence, each is duplicated, updated, returned.
        if (self._key is not None):
            # This node matches key. Return duplicate with new value
            return func(self._key, func(key, value), self._children)
        else:
            # Continue search using hashbits to pick direction
            child_num = hashbits & hamt.MASK
            # Copy can reuse key/value. Child list gets updated, so duplicate
            copy = hamt(self._key, self._value, list(self._children))
            if (copy._children[child_num] == None):
                # End of search, key not found, add new node
                copy._children[child_num] = hamt(key, value)
            else:
                # Continue by asking appropriate child to set key/value
                copy._children[child_num] = copy._children[child_num].     \
                                    _set(key, value, hashbits >> hamt.BITS)
            return copy  
    
    
    def map(self, func):
    #If current node is not empty, then we operate on it.
        if(self._key is not None):
            #self._value = self._value.func
            return func(self.key, self._value)
            #return func(self._key, func(key, value), self._children)
            for i in range(hamt.DEG):
                #If child node is not empty, then we operate on it.
                if(self._children[i] is not None):
                    func(self._children[i].key, self._children[i]._value)
                #if(self._children[i] is None):    
                    #s = s + "X"
                #If child node is empty, then we do nothing.
                else:
                    copy._children[child_num] = hamt(key, value)
                    #s = s + str(self._children[i])
        return copy
    '''
    #print(f.map(lambda k, v: str(k) + str(v)))
    
    def len(self):
        count = 0
        #print("count: " + str(count))
        if(self._key is not None):
            #print('if(self._key is not None):')
            count += 1
            #print("count: " + str(count))
        #s = "[({},{})".format(str(self._key),str(self._value))
        for i in range(hamt.DEG):
            #print('for i in range(hamt.DEG):')
            #print('i: ' + str(i))
            if (self._children[i] is None):
                #print('if (self._children[i] at '+ str(i) + ' is None):')
                #print('count += 0')
                count += 0
                #s = s + "X"
            else:
                #count += 1
                count += self._children[i].len()
                #print('else:')
                #print('count += self._children[i].len()')
                #print("count: " + str(count))
                #s = s + str(self._children[i])
        return count
    
    def get(self, key):
        # Pass key/value and hashbits to recursive helper
        return self._get(key, hash(key))
    
    #Returns what the value k is mapped-to or None if k is not a key in the HAMT
    def _get_v00(self, key, hashbits):
        if (self._key == key): #If the current node has the key.
            #This node matches key. Return duplicate with new value
            #return hamt(self._key, value, self._children)
            return self._value
        else:
            # Continue search using hashbits to pick direction
            child_num = hashbits & hamt.MASK
            #hashbits - basically the [00,01,10,11] paths for the nodes
            #hamt.mask - what is used to determine paths
            #Copy can reuse key/value. Child list gets updated, so duplicate
            copy = hamt(self._key, self._value, list(self._children))
            if (copy._children[child_num] == None):#If child node is none.
            
                #End of search, key not found, return None
                #^^^^^^^^^^^^copy._children[child_num] = hamt(key, value)
                return None
            else: #If child node is not none.
                #Continue by asking appropriate child to set key/value
                copy._children[child_num] = copy._children[child_num].     \
                                    _get(key, hashbits >> hamt.BITS)                        
            return copy
    
    def _get_01(self, key, hashbits):
        if(self._key == key):
            return self._value
        else:
            child_num = hashbits & hamt.MASK
            if self._children[child_num] is not None:
                return self._children[child_num]._get(key, hashbits >> hamt.BITS)
            else:
                return None
    '''        
    def _get(self, key, hashbits):
        child_num = hashbits & hamt.MASK
        print("hashbits: {}".format(bin(hashbits)))
        print("mask: {}".format(bin(hamt.MASK)))
        print("child_num: {}".format(bin(child_num)))
        print("current node key: {},looking for: {}".format(self._key, key))
        if(self._key == key):
            print("is key:{} key: {}".format(self._key, key))
            return self._value
        elif (self._children[child_num] is not None):
            print("is key:{} key: {}".format(self._key, key))
            print("searching the child nodes!")
            return self._children[child_num]._get(key, hashbits >> hamt.BITS)
        else:
            print("Key not found!")
            return None
    '''
    
    def get(self, key):
        # Pass key/value and hashbits to recursive helper
        return self._get(key, hash(key))
    

    
    def _get(self, key, hashbits):
        child_num = hashbits & hamt.MASK
        if(self._key == key):
            return self._value
        elif (self._children[child_num] is not None):
            return self._children[child_num]._get(key, hashbits >> hamt.BITS)
        else:
            return None
            
a = hamt("A", "a")
print("hamt")
print(a)
b = a.set("B", "b")
print("b = a.set(B, b)")
print(b)
c = a.set("C", "c")
print("c = b.set(C, c)")
print(c)
d = a.set("D", "d")
print("d = c.set(D, d)")
print(d)
e = a.set("E", "e")
print("e = c.set(E, e)")
print(e)
f = a.set("F", "f")
print("f = e.set(F, f)")
print(c)
#g = f.set("G", "g")
#print("g = f.set(G, g)")

#print(g)

#print(f.get("F"))
#print(f.len())
#print(f.map(lambda k, v: str(k) + str(v)))
#print(f.map(lambda k, v: k + v))
#f.map(lambda k, v: k + v)