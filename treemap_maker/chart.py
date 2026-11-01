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