with open('new.txt', 'r', encoding='utf-8') as f:
    res = [f'{line}. {"".join(count.split())} - {len(count.split())} слов' for line, count in enumerate(f, 1)]
    print(*res, f"Всего строк - {len(res)}.", sep='\n') #по умолчанию sep=' '
