packets = input("Введите 0 и 1: ")

if len(packets) < 5:
    print("Слишком коротко! Нужно минимум 5 символов")
    exit()

for char in packets:
    if char not in "01":
        print("Можно вводить только 0 и 1!")
        exit()

# Подсчеты
total = len(packets)
lost = packets.count('0')
max_streak = 0
current = 0

for char in packets:
    if char == '0':
        current += 1
        if current > max_streak:
            max_streak = current
    else:
        current = 0

percent = (lost / total) * 100


if percent <= 1:
    quality = "отличное"
elif percent <= 5:
    quality = "хорошее"
elif percent <= 10:
    quality = "удовлетворительное"
elif percent <= 20:
    quality = "плохое"
else:
    quality = "критическое"

print(f"Всего пакетов: {total}")
print(f"Потеряно: {lost}")
print(f"Самая длинная цепочка потерь: {max_streak}")
print(f"Процент потерь: {percent:.1f}%")
print(f"Качество: {quality}")