class node:
    def __init__(self, data):
        self.data = data
        self.children = None
    
    def add_child(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)
        
    def is_leaf(self):
        return self.children == None

class scanner:
    # toks[i] must evaluate to the i-th token in the token stream.
    # Assumes toks does not change during parsing
    def __init__(self,toks):
        self._toks = toks
        self._i = 0
    
    # If no more tokens exist or current token isn't s, raise exception.
    # Otherwise pass over the current one and move to the next.
    def match(self,s):
        if (self._i < len(self._toks)) and (self._toks[self._i] == s):
            self._i += 1
        else:
            raise Exception
            
    # If any tokens remain return the current one. If no more, return None.
    def next(self):
        if self._i < len(self._toks):
            return self._toks[self._i]
        else:
            return None

def parseD(toks):
    rval = node('D')
    tok = toks.next()
    if tok == '(':
        # Match tok (*'(') and add first child, a leaf node labeled tok
        toks.match('(')  #toks.match(tok)
        rval.add_child(node('('))
        # parseS and have resulting subtree be our second child
        rval.add_child(parseS(toks))
        # Match ")" and add third child, a leaf node labeled ")"
        toks.match(')')
        rval.add_child(node(')'))
    elif tok == 'a':
        # Match tok and add first child, a leaf node labeled tok
        toks.match('a')  #toks.match(tok)
        rval.add_child(node('a'))
    else:
        raise Exception
    return rval
def parseC(toks):
    rval = node('C')
    tok = toks.next()
    if tok in ('*', '/'):
        # Match tok and add first child, a leaf node labeled tok
        toks.match(tok) #toks.match(tok)
        rval.add_child(node(tok))
        # parseD and have resulting subtree be our second child
        rval.add_child(parseD(toks))
        # parseC and have resulting subtree be our second child
        rval.add_child(parseC(toks))
    elif (tok == None or tok in ('+', '-', ')')):
        rval.add_child(node(''))
    else:
        raise Exception
    return rval
def parseB(toks):
    rval = node('B')
    tok = toks.next()
    if tok in ('a', '('):
        # parseD and have resulting subtree be our second child
        rval.add_child(parseD(toks))
        # parseC and have resulting subtree be our second child
        rval.add_child(parseC(toks))
    else:
        raise Exception
    return rval
def parseA(toks):
    rval = node('A')
    tok = toks.next()
    if tok in ('+', '-'):
        # Match tok and add first child, a leaf node labeled tok
        toks.match(tok) #toks.match(tok)
        rval.add_child(node(tok))
        # parseB and have resulting subtree be our second child
        rval.add_child(parseB(toks))
        # parseA and have resulting subtree be our second child
        rval.add_child(parseA(toks))
    elif (tok == None or tok == ')'):
        rval.add_child(node(''))
    else:
        raise Exception
    return rval
def parseS(toks):
    rval = node('S')
    tok = toks.next()
    if tok in ('a', '('):
        # parseB and have resulting subtree be our second child
        rval.add_child(parseB(toks))
        # parseA and have resulting subtree be our second child
        rval.add_child(parseA(toks))
    else:
        # Unexpected token, so throw an exception
        raise Exception
    return rval
def parse(input):
    toks = scanner(input)
    rval = parseS(toks)
    if toks.next() != None:
        raise Exception
    return rval
try:
    parse("(a*a)")
except:
    print("Reject")
else:
    print("Accept")
    

def print_leaves(tree_node):
    if tree_node.is_leaf():#If node is a leaf.
        print(str(tree_node.data))#Print the leaf.
    else:#Else.
        for child in tree_node.children:#For each child node.
            print_leaves(child)#Recursively call the function on the child node.

my_tree = parse('(a)')
print_leaves(my_tree)


def num_leaves(tree_node):
    if tree_node.is_leaf():#If node is a leaf.
        return 1 #We return 1.
    else: #Else...
        counter = 0 #Start counter at 0.
        for child in tree_node.children: #For each child node.
            counter += num_leaves(child) #Recursively call the function on the child node and add its result to the counter.
        return counter #Return the counter result.

my_tree = parse('(a*a)')
print(num_leaves(my_tree))



'''
def num_leaves(tree_node):
    if tree_node.is_leaf():#If node is a leaf.
        count = 0
        count = count + 1
        print(count)
    else:
        for child in tree_node.children:#For each child node.
            num_leaves(child)#Recursively call the function on the child node.
'''           
'''        
def _num_leaves(tree_node, count):
    if tree_node.is_leaf():
        count = count + 1
        print(count)
    else:
        for child in tree_node.children:
            return _num_leaves(child, count + 1)
    
def num_leaves(tree_node):
    return _num_leaves(tree_node, 0)
'''
'''
def num_leaves(tree_node):
    count = 0
    if tree_node.is_leaf(): #If node is a leaf.
        count += 1 #Increase the count by one.
    for child in tree_node.children:#For each child node.
        num_leaves(child)
    return count
    
my_tree = parse('(a)')
num_leaves(my_tree)
   ''' 
'''
def num_leaves(tree_node):
    count = 0
    for child in tree_node.children:#For each child node.
        if tree_node.is_leaf():#If node is a leaf.
            count = count + 1
            print(count)
            #return count
        #else:
            #num_leaves(child)#Recursively call the function on the child node.
'''

#my_tree = parse('(a)')
#num_leaves(my_tree)
#print_leaves(my_tree)
