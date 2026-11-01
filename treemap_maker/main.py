
#Requesting data from the user
def get_data():
    print("Enter data for the chart")

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