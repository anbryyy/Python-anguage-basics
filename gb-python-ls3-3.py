def my_func(a, b, c):
    try:
        return sum((a, b, c)) - min(a, b, c)
    except TypeError:
        return 'Enter only numbers!'

print(my_func(1, 1, 2))