def draw_square(stdscr, x, y, size):
    for i in range(size):
        stdscr.addch(y, x + i, '█')         # Верхняя граница
        stdscr.addch(y + size - 1, x + i, '█') # Нижняя граница
        stdscr.addch(y + i, x, '█')         # Левый бок
        stdscr.addch(y + i, x + size - 1, '█') # Правый бок


def draw_circle(stdscr, center_x, center_y, radius):
    for y in range(center_y - radius, center_y + radius + 1):
        for x in range(center_x - radius, center_x + radius + 1):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                stdscr.addch(y, x, '█')





# # Получить размеры экрана
# max_y, max_x = stdscr.getmaxyx()

# # Размер и позиция квадрата
# size = 10
# x = (max_x - size) // 2
# y = (max_y - size) // 2

# # Проверка, чтобы квадрат вписывался в экран
# if x >= 0 and y >= 0 and x + size < max_x and y + size < max_y:
#     draw_circle(stdscr, x, y, size)                