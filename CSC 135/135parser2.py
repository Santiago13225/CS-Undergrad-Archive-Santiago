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

# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on a parse error.
#S' → S$
#S → BA
#A → +BA | -BA | λ
#B → DC
#C → *DC | /DC | λ
#D → a | (S)

#a+-*/()$
def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()      # Always pop top of stack
        tok = toks.next()      # None indicates token stream empty
        if top in ('a', '+', '-', '*', '/', '(', ')'):     # Matching stack top to token
            toks.match(top)
        #elif top == 'S' and tok == None: # test for next == $ 
            #pass # "pass" is how you say do nothing in Python
        elif top == 'S' and (tok in ('a', '(')): # S → BA must be the next
            stack.append('A')            # production to follow here
            stack.append('B')
        elif top == 'A' and tok == '+':  # A → +BA must be the next
            stack.append('A')            # production to follow here
            stack.append('B')
            stack.append('+')
        elif top == 'A' and tok == '-':  # A → -BA must be the next
            stack.append('A')            # production to follow here
            stack.append('B')
            stack.append('-')
        elif top == 'A' and (tok == None or tok == ')'): # A → λ must be the next
            pass                         # production to follow here
        elif top == 'B' and (tok == None or tok in ('a', '(')): # B → DC must be the next
            stack.append('C')            # production to follow here
            stack.append('D')
        elif top == 'C' and tok == '*':  # C → *DC must be the next
            stack.append('C')            # production to follow here
            stack.append('D')
            stack.append('*')
        elif top == 'C' and tok == '/':  # C → /DC must be the next
            stack.append('C')            # production to follow here
            stack.append('D')
            stack.append('/')
        elif top == 'C' and (tok == None or tok in ('+', '-', ')')):  # C → λ must be the next
            pass                          # production to follow here
        elif top == 'D' and tok == 'a':  # D → a must be the next
            stack.append('a')            # production to follow here
        elif top == 'D' and tok == '(':  # D → (S) must be the next
            stack.append(')')            # production to follow here
            stack.append('S')
            stack.append('(')
        else:
            raise Exception    # Unrecognized top/tok combination
    if toks.next() != None:
        raise Exception
try:
    parse("(a*a)")
except:
    print("Reject")
else:
    print("Accept")
