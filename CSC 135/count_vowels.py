stringA = "SOO beautiful"

#filters list
def count_vowelsHelper(listA):
    vowels = ['A', 'E', 'I', 'O', 'U'] 
    if (listA in vowels):
        return True
    else: 
        return False

def count_vowels(stringA):
    return len(list(filter(count_vowelsHelper, list(stringA.upper()))))

def count_vowels2(stringA):
    return len(list(filter(lambda c: c.upper() in "AEIOU", s)))
    
print('The filtered amount of letters are: ')
print(count_vowels(stringA))