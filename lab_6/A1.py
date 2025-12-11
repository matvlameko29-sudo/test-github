import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt



def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []  # Будет заполнено позже
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []


def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            # Для расстояния: если '0', то 0.0, иначе преобразуем в float
            distance_text = workout_elem.find('distance').text
            distance = 0.0 if distance_text == '0' else float(distance_text)

            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': distance,
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []


# ЗАДАЧА 1: ОБЩАЯ СТАТИСТИКА
def get_stats(users, workouts):
    """Расчет общей статистики по всем тренировкам"""
    total_workouts = len(workouts)
    total_users = len(users)

    total_calories = sum(workout['calories'] for workout in workouts)
    total_time = sum(workout['duration'] for workout in workouts) / 60.0
    total_distance = sum(workout['distance'] for workout in workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("==========================")
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print()

    return total_workouts, total_calories, total_time, total_distance


#ЗАДАЧА 2

def analyze_user_activity(users, workouts):
    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        user['workouts'] = user_workouts
        user['total_workouts'] = len(user_workouts)
        user['total_calories'] = sum(w['calories'] for w in user_workouts)
        user['total_time'] = sum(w['duration'] for w in user_workouts) / 60.0

    sorted_users = sorted(users, key=lambda x: x['total_workouts'], reverse=True)

    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, user in enumerate(sorted_users[:3], 1):
        print(f"{i}. {user['name']} ({user['fitness_level']}):")
        print(f"   Тренировок: {user['total_workouts']}")
        print(f"   Калорий: {user['total_calories']}")
        print(f"   Время: {user['total_time']:.1f} часов")
        print()

    return sorted_users


def analyze_workout_types(workouts):
    workout_types = {}
    for workout in workouts:
        workout_type = workout['type']
        if workout_type not in workout_types:
            workout_types[workout_type] = {
                'count': 0,
                'total_duration': 0,
                'total_calories': 0
            }

        workout_types[workout_type]['count'] += 1
        workout_types[workout_type]['total_duration'] += workout['duration']
        workout_types[workout_type]['total_calories'] += workout['calories']

    total_workouts = len(workouts)

    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")

    type_order = ['бег', 'силовая тренировка', 'велосипед', 'плавание', 'ходьба']

    for workout_type in type_order:
        if workout_type in workout_types:
            data = workout_types[workout_type]
            percentage = (data['count'] / total_workouts) * 100
            avg_duration = data['total_duration'] / data['count']
            avg_calories = data['total_calories'] / data['count']
            print(f"{workout_type.capitalize()}: {data['count']} тренировок ({percentage:.1f}%)")
            print(f"Средняя длительность: {avg_duration:.0f} мин")
            print(f"Средние калории: {avg_calories:.0f} ккал")
    print()
    return workout_types

def find_user_workouts(users, user_name):
    user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if user:
        return user['workouts']
    return []

def analyze_user(users, user_name):
    user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if not user:
        print(f"Пользователь {user_name} не найден")
        return
    workouts = user['workouts']
    if not workouts:
        print(f"У пользователя {user_name} нет тренировок")
        return

    total_workouts = len(workouts)
    total_calories = sum(w['calories'] for w in workouts)
    total_time = sum(w['duration'] for w in workouts) / 60.0
    total_distance = sum(w['distance'] for w in workouts)
    avg_calories = total_calories / total_workouts
    type_counts = {}
    for workout in workouts:
        workout_type = workout['type']
        type_counts[workout_type] = type_counts.get(workout_type, 0) + 1

    favorite_type = max(type_counts, key=type_counts.get)

    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("=" * 60)
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {total_workouts}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print(f"Средние калории за тренировку: {avg_calories:.0f}")
    print(f"Любимый тип тренировки: {favorite_type}")
    print()

#ЗАДАЧА 3

def visualize_data(users, workouts, workout_types):

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    labels1 = []
    sizes1 = []
    colors1 = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7']

    for i, (workout_type, data) in enumerate(workout_types.items()):
        labels1.append(f"{workout_type}\n({data['count']})")
        sizes1.append(data['count'])

    axes[0, 0].pie(sizes1, labels=labels1, colors=colors1[:len(labels1)], autopct='%1.1f%%', startangle=90)
    axes[0, 0].set_title('Круговая диаграмма типов тренировок', fontweight='bold')
    user_names = [user['name'] for user in users]
    workout_counts = [user['total_workouts'] for user in users]
    bars1 = axes[0, 1].bar(user_names, workout_counts, color='skyblue')
    axes[0, 1].set_title('Активность пользователей', fontweight='bold')
    axes[0, 1].set_xlabel('Пользователи')
    axes[0, 1].set_ylabel('Количество тренировок')
    axes[0, 1].tick_params(axis='x', rotation=45)
    for bar in bars1:
        height = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width() / 2., height + 0.1,
             f'{int(height)}', ha='center', va='bottom')

    avg_calories_per_workout = []
    for user in users:
        if user['total_workouts'] > 0:
            avg = user['total_calories'] / user['total_workouts']
        else:
            avg = 0
        avg_calories_per_workout.append(avg)

    bars2 = axes[1, 0].bar(user_names, avg_calories_per_workout, color='lightgreen')
    axes[1, 0].set_title('Эффективность тренировок', fontweight='bold')
    axes[1, 0].set_xlabel('Пользователи')
    axes[1, 0].set_ylabel('Средние калории за тренировку')
    axes[1, 0].tick_params(axis='x', rotation=45)

    for bar in bars2:
        height = bar.get_height()
        axes[1, 0].text(bar.get_x() + bar.get_width() / 2., height + 5,
                        f'{int(height)}', ha='center', va='bottom')

    total_calories_per_user = [user['total_calories'] for user in users]

    bars3 = axes[1, 1].bar(user_names, total_calories_per_user, color='salmon')
    axes[1, 1].set_title('Общие затраченные калории', fontweight='bold')
    axes[1, 1].set_xlabel('Пользователи')
    axes[1, 1].set_ylabel('Калории')
    axes[1, 1].tick_params(axis='x', rotation=45)

    for bar in bars3:
        height = bar.get_height()
        axes[1, 1].text(bar.get_x() + bar.get_width() / 2., height + 10,
                        f'{int(height)}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


  #ОСНОВНАЯ ПРОГРАММА

def main():
    print("=" * 60)
    print("АНАЛИЗ ДАННЫХ ФИТНЕС-ТРЕКЕРА")
    print("=" * 60)
    print()

    print("Загрузка данных...")
    users = load_users_data()
    workouts = load_workouts_data()

    if not users or not workouts:
        print("Ошибка загрузки данных. Проверьте наличие файлов.")
        return

    print("\nЗАДАЧА 1: ОБЩАЯ СТАТИСТИКА")
    print("-" * 40)
    get_stats(users, workouts)

    print("\nЗАДАЧА 2: АНАЛИЗ АКТИВНОСТИ")
    print("-" * 40)

    sorted_users = analyze_user_activity(users, workouts)

    workout_types = analyze_workout_types(workouts)

    user_name = "Борис"
    print(f"Поиск тренировок пользователя: {user_name}")
    user_workouts = find_user_workouts(sorted_users, user_name)
    print(f"Найдено тренировок: {len(user_workouts)}")
    print()

    print("Детальный анализ пользователя:")
    analyze_user(sorted_users, user_name)

    print("\nЗАДАЧА 3: ВИЗУАЛИЗАЦИЯ ДАННЫХ")
    print("-" * 40)
    print("Построение диаграмм...")

    visualize_data(sorted_users, workouts, workout_types)

    print("\nАнализ всех пользователей:")
    print("-" * 40)
    for user in sorted_users:
        analyze_user(sorted_users, user['name'])


if __name__ == "__main__":
    main()