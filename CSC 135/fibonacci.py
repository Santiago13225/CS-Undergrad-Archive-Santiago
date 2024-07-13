def by_six(n):
    number = n
    if number % 2 == 0:
        if number % 3 == 0:
            print("Divisible by 6.")
            
    elif number % 3 == 0:
        print("Odd.")
    """    
    if number % 2 == 0:
        if number % 3 == 0:
            print("Divisible by 6.")
        else:
            print("Odd.")
    """
return_value = by_six(12)#Divisible by 6
print('{}'.format(return_value))

return_value = by_six(42)#Divisible by 6
print('{}'.format(return_value))

return_value = by_six(5)#Odd
print('{}'.format(return_value))

return_value = by_six(-127)#Odd
print('{}'.format(return_value))

return_value = by_six(14)#No_Output
print('{}'.format(return_value))

return_value = by_six(200)#No_Output
print('{}'.format(return_value))