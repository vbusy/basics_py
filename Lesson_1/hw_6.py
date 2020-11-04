a = int(input("Kilometers: "))
b = int(input("Result: "))
c = 1
while True:
    if a <= b:
        a = a + (a * 10 / 100)
        c = c + 1
    else:
        break
print(c)