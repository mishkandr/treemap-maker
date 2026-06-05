import matplotlib.pyplot as plt
import squarify

def get_user_data():
    """Функция для запроса данных у пользователя"""
    print("--- Ввод данных для Treemap ---")
    
    # Запрос названий категорий
    raw_labels = input("Введите названия категорий через запятую (напр: А, Б, В): ")
    labels = [item.strip() for item in raw_labels.split(',')]
    
    # Запрос числовых значений
    raw_sizes = input(f"Введите значения для {len(labels)} категорий через запятую: ")
    try:
        sizes = [float(item.strip()) for item in raw_sizes.split(',')]
    except ValueError:
        print("Ошибка: вводите только числа!")
        return None, None

    if len(labels) != len(sizes):
        print("Ошибка: количество названий и чисел не совпадает!")
        return None, None
        
    return labels, sizes

# 1. Получаем данные
labels, sizes = get_user_data()

if labels and sizes:
    # 2. Построение
    plt.figure(figsize=(10, 6))
    
    # Цвета генерируются автоматически в зависимости от кол-ва элементов
    colors = plt.cm.Spectral( [i/float(len(labels)) for i in range(len(labels))] )
    
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

    plt.title("Ваш кастомный Treemap")
    plt.axis('off')
    plt.show()