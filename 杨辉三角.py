# 杨辉三角算法思想 每个数字等于上一行对应两个数字之和
def tri():
    T=[1]
    while True:
        yield T            #返回T
        T.append(0)        # m每次在最后一位加0 用于T续叠加
        T=[T[i-1]+T[i] for i in range(len(T))]

def print_triangle(x):
        a = 0
        for t in tri():  #这里可以每次调用一个N（得力于Yield函数）
            print(t)
            if a ==x:
                break
print_triangle(10) #打印10行

