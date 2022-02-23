# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (500, 500)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
for j in range(0, 1000, 50):
    for i in range(10):
        sd.rectangle(sd.get_point(100 * i, j), sd.get_point(100 + i * 100, j + 50), width=3, color=[11, 212, 12])

sd.pause()
