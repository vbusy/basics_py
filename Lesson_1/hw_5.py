procceds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if procceds > costs:
    print("Result = profit")
    profitability = (procceds - costs) / procceds
    employees = int(input("The number of employees: "))
    profit_one = int(procceds / employees)
    print(profit_one)
else:
    print("Result = damages")