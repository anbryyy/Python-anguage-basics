revenue = int(input("Enter the company's revenue for the month: "))
expenses = int(input("Enter the company's monthly expenses: "))
if revenue > expenses:
    profit = revenue - expenses
    print(f"The company's profit for the month was: {profit}")
    profitability = (profit/revenue)*100
    print(f"Profitability was {profitability:.2f}%")

    number_of_employees = int(input('Enter the number of employees of the company: '))
    profit_per_employee = profit/number_of_employees
    print(f"Profit per employee was {profit_per_employee:.2f}")

elif revenue < expenses:
    loss = expenses - revenue
    print(f"The company's loss for the month was: {loss}")
else:
    revenue = expenses
    print("The company didn't earn anything")



