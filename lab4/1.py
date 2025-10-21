import random
import time

n = int(input("Сколько примеров? "))

correct = 0
total_time = 0

print()

for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    right_answer = a * b

    while True:
        start = time.time()
        user_answer = input(f"{a} × {b} = ")
        time_spent = time.time() - start

        try:
            user_answer = int(user_answer)
            break
        except:
            print("Введите целое число!")

    if user_answer == right_answer:
        print(f"Верно! (Время: {time_spent:.1f} сек)")
        correct += 1
    else:
        print(f"Неверно! Правильно: {right_answer} (Время: {time_spent:.1f} сек)")

    total_time += time_spent
    print()


avg_time = total_time / n
percent = (correct / n) * 100

print("---")
print("СТАТИСТИКА:")
print("---")
print(f"Общее время: {total_time:.1f} сек")
print(f"Среднее время: {avg_time:.1f} сек")
print(f"Правильных: {correct}/{n}")
print(f"Процент: {percent:.1f}%")