"""
正整数的反转

Version: 0.1
Author: Brandon Hoo
Date:2020-01-13
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)