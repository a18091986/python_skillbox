# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7

def size_compare(paper_x, paper_y):
    if paper_x > envelop_x or paper_y > envelop_y:
        print(f'Для {paper_x}, {paper_y}: не поместится')
        return False
    print(f'Для {paper_x}, {paper_y}: поместится')

paper_x, paper_y = 8, 9
size_compare(paper_x, paper_y)
paper_x, paper_y = 9, 8
size_compare(paper_x, paper_y)
paper_x, paper_y = 6, 8
size_compare(paper_x, paper_y)
paper_x, paper_y = 8, 6
size_compare(paper_x, paper_y)
paper_x, paper_y = 3, 4
size_compare(paper_x, paper_y)
paper_x, paper_y = 11, 9
size_compare(paper_x, paper_y)
paper_x, paper_y = 9, 11


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9

print(f'Размер отверстия: {hole_x, hole_y}')

def hole_brick(brick_x, brick_y, brick_z):
    bx = brick_x
    by = brick_y
    bz = brick_z
    hx = hole_x
    hy = hole_y
    if hx >= bx and (hy >= by or hy >= bz):
        print(f'Кирпич c размерами {brick_x, brick_y, brick_z} пройдет в отверстие {hole_x, hole_y}')
    elif hx >= by and (hy >= bx or hy >= bz):
        print(f'Кирпич c размерами {brick_x, brick_y, brick_z} пройдет в отверстие {hole_x, hole_y}')
    elif hx >= bz and (hy >= bx or hy >= by):
        print(f'Кирпич c размерами {brick_x, brick_y, brick_z} пройдет в отверстие {hole_x, hole_y}')
    else:
        print(f'Кирпич c размерами {brick_x, brick_y, brick_z} не пройдет в отверстие {hole_x, hole_y}')


brick_x, brick_y, brick_z = 11, 10, 2
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 2, 10
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 11, 2
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 2, 11
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 10, 11
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 11, 10
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 5, 6
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 5
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 5
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 5, 3
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 6, 3
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 3, 6
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 3, 6
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 6, 3
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 11, 3
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 11
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 11
hole_brick(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 11, 6
