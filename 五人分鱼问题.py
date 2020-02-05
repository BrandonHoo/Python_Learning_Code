# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

def main():
    fish=1          #初始化鱼的数目
    while True:
        total,enough=fish,True
        for _ in range(5):
            if (total-1)%5==0:    #条件验证
                total=(total-1)//5*4  #总数循环相加
            else:
                enough=False
                break
            if enough:
                print(f"总共有{fish}条鱼")
            fish+=1

if __name__ == "__main__":
    main()

