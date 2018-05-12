x = float(input("Enter hours: "))
y = float(input("Enter rate: "))
if x <= 40:
    print(x * y)
else:
    if x > 40:
        print((x - 40) * 15 + (40 * y))
