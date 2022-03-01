def div(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print('Division by zero is forbidden')
    except ValueError:
        print('You should enter integers')


print(div(input(), input()))