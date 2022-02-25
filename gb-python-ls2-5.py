a = [1, 9, 9, 7, 2, 0, 0, 1]
new_num = int(input('Enter a new rating: '))
i = 0
for n in a:
    if new_num <= n:
        i += 1
a.insert(i, new_num)
print(a)