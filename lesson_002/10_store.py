#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# Lamps
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = int(lamps_item['quantity'])
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Tables
tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
tables_cost += store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
table_code = goods['Стол']
table_item_first = store[table_code][0]
table_item_second = store[table_code][1]
table_quantity = table_item_first['quantity'] + table_item_second['quantity']
print('Стол -', table_quantity, 'шт, стоимость', tables_cost, 'руб')

# Sofas
sofas_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofas_cost += store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sofa_code = goods['Диван']
sofa_item_first = store[sofa_code][0]
sofa_item_second = store[sofa_code][1]
sofa_quantity = sofa_item_first['quantity'] + sofa_item_second['quantity']
print('Диван -', sofa_quantity, 'шт, стоимость', sofas_cost, 'руб')\

# Chair
chairs_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chairs_cost += store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chairs_cost += store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
chair_code = goods['Стул']
chair_item_first = store[chair_code][0]
chair_item_second = store[chair_code][1]
chair_item_third = store[chair_code][2]
chair_quantity = chair_item_first['quantity'] + chair_item_second['quantity'] + chair_item_third['quantity']
print('Стул -', chair_quantity, 'шт, стоимость', chairs_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
