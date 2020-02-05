def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # (a,b)=(b,a+b)
        yield a          # 迭代生成器，将对象变为一个生成函数，相当于return+生成器


def main():
    for val in fib(20):
        print(val)

'''
#递归方法

def fib_recursive(n)
    if n<=1:
        return 1
    return fib_recursive(n-1)+fib_recursive(n-2)

    for i in range(20):
        print(fib_recursive(i),end='')

'''

'''
# 循环方法

def fib_cycle(n)
    a,b=0,1
    for i in range(n):
        print(b,end='')
        a,b=b,a+b

fib_cycle(20)

'''
if __name__ == '__main__':
    main()


 递归方法


