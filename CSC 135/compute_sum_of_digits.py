num = int(input('Type an integer: '))

sum = 0

while(num != 0):
    sum += (num % 10)
    num //= 10

print('Digit sum is {}'.format(sum))