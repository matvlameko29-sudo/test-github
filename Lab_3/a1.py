x1 = float(input('Введите значение'))
y1 = float(input('Введите значение'))
x2 = float(input('Введите значение'))
y2 = float(input('Введите значение'))

if x1 > 0 and y1 > 0:
    quarter1 = "I"
elif x1 < 0 and y1 > 0:
    quarter1 = "II"
elif x1 < 0 and y1 < 0:
    quarter1 = "III"
else:
    quarter1 = "IV"

if x2 > 0 and y2 > 0:
    quarter2 = "I"
elif x2 < 0 and y2 > 0:
    quarter2 = "II"
elif x2 < 0 and y2 < 0:
    quarter2 = "III"
else:
    quarter2 = "IV"

if quarter1 == quarter2:
    print(f"Yes, {quarter1}")
else:
    print("No")