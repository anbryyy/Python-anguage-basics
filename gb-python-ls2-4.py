a = input('Enter few words separated by a space: ').split()

for i, word in enumerate(a,1):
    print(f'{i} {word[:10]}')