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
'''
# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on a parse error.
# S → aSa
# S → bSb
# S → x
def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()      # Always pop top of stack
        tok = toks.next()      # None indicates token stream empty
        if tok == None:        # Running out of tokens is error in this grammar
            raise Exception
        elif top in ('a', 'b', 'x'):     # Matching stack top to token
            toks.match(top)
        elif top == 'S' and tok == 'a':  # S -> aSa must be the next
            stack.append('a')            # production to follow here
            stack.append('S')
            stack.append('a')
        elif top == 'S' and tok == 'b':  # S -> bSb must be the next
            stack.append('b')            # production to follow here
            stack.append('S')
            stack.append('b')
        elif top == 'S' and tok == 'x':  # S -> x must be the next
            stack.append('x')            # production to follow here
        else:
            raise Exception    # Unrecognized top/tok combination
    if toks.next() != None:
        raise Exception

try:
    parse("axa")
except:
    print("Reject")
else:
    print("Accept")
'''

# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on a parse error.
# S → <AB
# A → aAb | b
# B → bB | >
def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()      # Always pop top of stack
        tok = toks.next()      # None indicates token stream empty
        if tok == None:        # Running out of tokens is error in this grammar
            raise Exception
        elif top in ('a', 'b', '<','>'):     # Matching stack top to token
            toks.match(top)
        elif top == 'S' and tok == '<':  # S -> <AB must be the next
            stack.append('B')            # production to follow here
            stack.append('A')
            stack.append('<')
        elif top == 'A' and tok == 'a':  # A → aAb must be the next
            stack.append('b')            # production to follow here
            stack.append('A')
            stack.append('a')
        elif top == 'A' and tok == 'b':  # A → b must be the next
            stack.append('b')            # production to follow here
        elif top == 'B' and tok == 'b':  # B → bB must be the next
            stack.append('B')            # production to follow here
            stack.append('b')
        elif top == 'B' and tok == '>':  # B → > must be the next
            stack.append('>')            # production to follow here
        else:
            raise Exception    # Unrecognized top/tok combination
    if toks.next() != None:
        raise Exception
try:
    parse("<aabbb>")
except:
    print("Reject")
else:
    print("Accept")
