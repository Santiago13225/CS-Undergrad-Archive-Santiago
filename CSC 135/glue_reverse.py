listA = ["the", "quick", "brown", "fox"]


def glue_reverse(list1):
    '''
    if(len(list1) == 0):
        return ""
    elif(len(list1) == 1):
        return str(list1[0])
    else:
    '''
    return ''.join([str(item) for item in (list1[::-1])])

string1 = glue_reverse(listA)
#listB = listA[::-1]
print('The reversed list of strings are: ')
print(string1)