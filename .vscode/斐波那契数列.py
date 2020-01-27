def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # (a,b)=(b,a+b)
        yield a          # 迭代生成器，将对象变为一个生成函数，相当于return+生成器


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
