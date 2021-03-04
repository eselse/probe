#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Tatiana", "Dmitriy", "Roman", "Anna"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Tatiana", 170],
    ["Dmitriy", 165],
    ["Roman", 180],
    ["Anna", 160],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("The height of my grandfather:", my_family_height[1][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
general_height = my_family_height[0][1] + \
                 my_family_height[1][1] + \
                 my_family_height[2][1] + \
                 my_family_height[3][1]
print("The general height of my family is:", general_height)
