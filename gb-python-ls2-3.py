l_seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
d_seasons = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
             10: 'осень', 11: 'осень', 12: 'зима'}
month = int(input('Enter the month number: '))
if month in d_seasons:
    print(l_seasons[month - 1])
    print(d_seasons[month])
elso:
    print('Invalid value')
