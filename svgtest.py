from random import randint
import pygal


def roll_dice(n=1):
	total = 0
	for _ in range(n):
		total += randint(1, 6)
	return total


def main():
    results = []
    # 将两颗色子摇10000次记录点数
    for _ in range(10000):
        face = roll_dice(2)
        results.append(face)
    freqs = []
    # 统计2~12点各出现了多少次
    for value in range(2, 13):
        freq = results.count(value)
        freqs.append(freq)
    # 绘制柱状图
    hist = pygal.Bar()
    hist.title = 'Result of rolling two dice'
    hist.x_labels = [x for x in range(2, 13)]
    hist.add('Frequency', freqs)
    # 保存矢量图
    hist.render_to_file('result.svg')


if __name__ == '__main__':
    main()