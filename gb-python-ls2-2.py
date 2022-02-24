a = list(input('Write something:) ').split())
print(a)

for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]

print(a)