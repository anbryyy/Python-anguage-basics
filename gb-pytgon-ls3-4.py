def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('the program only works with real x and integer y')
        return
    if x <= 0 or y >= 0:
        print('the program only works with positive x and negative y')
        return
    return x ** y

print(round(my_func(1, -1), 2))
