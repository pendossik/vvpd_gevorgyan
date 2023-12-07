def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x1 > x4 or y2 > y3 or y1 < y4:
        return 'Прямоугольники не пересекаются'
    left_x = max(x1, x3)
    right_x = min(x2, x4)
    top_y = min(y1, y3)
    bottom_y = max(y2, y4)
    intersection_area = (right_x - left_x) * (top_y - bottom_y)
    return intersection_area


def union(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x1 > x4 or y2 > y3 or y1 < y4:
        return 'Прямоугольники не пересекаются'
    area_1 = (x2 - x1) * (y1 - y2)
    area_2 = (x4 - x3) * (y3 - y4)
    intersection_area = intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    union_area = area_1 + area_2 - intersection_area
    return union_area


def validate_number_input(prompt):
    '''Проверяет на целочисленность'''
    while True:
        number = input(prompt)
        if not number:
            print("Некорректный ввод. Пожалуйста, введите число.")
            continue
        try:
            return int(number)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def menu():
    print('- - - - - - - - - - - - - - - - - - - - - -')
    print('Список комманд:')
    print('\t[0] - Выход')
    print('\t[1] - Ввести новые координаты прямоугольников')
    print('\t[2] - Найти площадь пересечения двух прямоугольников')
    print('\t[3] - Найти площадь объединения двух прямоугольников')
    print('- - - - - - - - - - - - - - - - - - - - - -')


def main():
    x1 = validate_number_input('Введите координату x левого верхнего угла 1 прямоугольника: ')
    y1 = validate_number_input('Введите координату y левого верхнего угла 1 прямоугольника: ')
    x2 = validate_number_input('Введите координату x правого нижнего угла 1 прямоугольника: ')
    y2 = validate_number_input('Введите координату y правого нижнего угла 1 прямоугольника: ')
    x3 = validate_number_input('Введите координату x левого верхнего угла 2 прямоугольника: ')
    y3 = validate_number_input('Введите координату y левого верхнего угла 2 прямоугольника: ')
    x4 = validate_number_input('Введите координату x правого нижнего угла 2 прямоугольника: ')
    y4 = validate_number_input('Введите координату y правого нижнего угла 2 прямоугольника: ')
    while True:
        menu()
        command = input()
        match command:
            case '0':
                print('Программа завершена')
                break
            case '1':
                x1 = validate_number_input('Введите координату x левого верхнего угла 1 прямоугольника: ')
                y1 = validate_number_input('Введите координату y левого верхнего угла 1 прямоугольника: ')
                x2 = validate_number_input('Введите координату x правого нижнего угла 1 прямоугольника: ')
                y2 = validate_number_input('Введите координату y правого нижнего угла 1 прямоугольника: ')
                x3 = validate_number_input('Введите координату x левого верхнего угла 2 прямоугольника: ')
                y3 = validate_number_input('Введите координату y левого верхнего угла 2 прямоугольника: ')
                x4 = validate_number_input('Введите координату x правого нижнего угла 2 прямоугольника: ')
                y4 = validate_number_input('Введите координату y правого нижнего угла 2 прямоугольника: ')
            case '2':
                print(f'Площадь пересечения прямоугольников равна {intersection(x1, y1, x2, y2, x3, y3, x4, y4)}')
            case '3':
                print(f'Площадь объединения прямоугольников равна {union(x1, y1, x2, y2, x3, y3, x4, y4)}')
            case _:
                print('Неверная команда')


if __name__ == '__main__':
    main()

print(intersection(1, 4, 4, 2, 3, 3, 6, 1))