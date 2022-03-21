with open('new-3.txt', 'r', encoding='utf-8') as f:
    employees = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees.values()) / len(employees), 3)}\n'
          f'Employees with salary less then 20k {[e[0] for e in employees.items() if e[1] < 20000]}')
