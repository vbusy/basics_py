n = int(input("Введите целое положительное число: "))
n_max = 0
while n > 0:
    remainder = n % 10
    if n_max < remainder:
        n_max = remainder
    n = n // 10
print(n_max)