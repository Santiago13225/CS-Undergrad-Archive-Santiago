from functools import reduce

words = ["four", "score", "and", "seven", "years", "ago"]

def three_four_letter_words(list1):
    '''
    if(len(list1) == 1):
        return list1[0]
    else:
    '''
    return list(filter(three_four_letter_wordsHelper, list1))

def three_four_letter_wordsHelper(list1):
    if (len(list1) == 3 or len(list1) == 4):
        return True
    else: 
        return False
    
words2 = three_four_letter_words(words)

print(words2)