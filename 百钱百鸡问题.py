"""
《百钱百鸡》问题

Version: 0.1
Author: Brandon Hoo
Date:2020-01-13

穷举法例子：
对所有可能进行验证，得出所有正确的答案， （循环+验证条件）
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))