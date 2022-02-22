from pprint import pprint
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

def dist_from_to(city1, city2):
    x1 = sites[city1][0]
    x2 = sites[city2][0]
    y1 = sites[city1][1]
    y2 = sites[city2][1]
    out_dict = {f'{city1}-{city2}': pow(pow(x1-x2,2) + pow(y1-y2,2),0.5),
                f'{city2}-{city1}': pow(pow(x1-x2,2) + pow(y1-y2,2),0.5)}
    return out_dict



distances = {}
distances.update(dist_from_to('Moscow', 'London'))
distances.update(dist_from_to('Moscow', 'Paris'))
distances.update(dist_from_to('London', 'Paris'))


pprint(distances)




