number = int(input('Введите целое роложительное число: '))
num_stat = number
integer = 0
while number > 0:
    rem = number % 10
    print(rem, end=" ")
    integer = rem if rem > integer else integer
    number = number // 10
    print('')
print('%d наибольшая цифра в числе %d' % (integer, num_stat))


