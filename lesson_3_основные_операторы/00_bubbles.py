# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius -= 10
    sd.circle(center_position=point, radius = radius, width = 2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step_x, step_y, c_1 = 255, c_2 = 255, c_3 = 255):
    point = sd.get_point(point.x + step_x, point.y + step_y)
    sd.circle(center_position=point, radius=50, width=2, color=[c_1, c_2, c_3])

bubble(point, 100, 200)

# Нарисовать 10 пузырьков в ряд

for i in range(1,1000,100):
    bubble(point, i, 0)

# Нарисовать три ряда по 10 пузырьков

for j in range(200,500,100):
    for i in range(1,1000,100):
        bubble(point, i, j)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for i in range(100):
    a = random.randint(100, 500)
    b = random.randint(100, 500)
    c_1 = random.randint(0,255)
    c_2 = random.randint(0, 255)
    c_3 = random.randint(0, 255)
    bubble(point, a, b, c_1, c_2, c_3)

sd.pause()


