prev = int(input())
curr = int(input())

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

if used <= 300:
    payment = 21.0
elif used <= 600:
    payment = 21.0 + (used - 300) * 0.065
elif used <= 800:
    payment = 21.0 + 300 * 0.065 + (used - 600) * 0.045
else:
    payment = 21.0 + 300 * 0.065 + 200 * 0.045 + (used - 800) * 0.025

if used > 0:
    avg_price = payment / used
else:
    avg_price = 0

print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{prev} {curr} {used} {payment:.2f} {avg_price:.2f}")