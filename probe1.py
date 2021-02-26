"""
This simple script shows numbers from 1 to 100
from that we can extract quadratic root and then multiplied by itself
"""
for i in range(100):
    number = i+1
    if (number ** 0.5) * (number ** 0.5) == number:
        print(number)