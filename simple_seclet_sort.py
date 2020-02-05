def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):             #range 第一个参数是开始值  第二个参数是结束值 第三个参数是步长
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

    # lanbda 表达式的使用

    '''
    # 数组方法实现
    def select_sort(array):
        lenth = len(array)
    for i in range(lenth):
        for j in range(i, lenth):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array

    '''