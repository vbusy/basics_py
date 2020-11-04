n = int(input("Введите время в секуднах:"))
nmin = n // 60
hours = nmin // 60
minutes = nmin % 60
seconds = n % 60
time = f"{hours:02}:{minutes:02}:{seconds:02}"
print(time)