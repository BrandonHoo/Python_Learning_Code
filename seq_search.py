def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):          #enumerate将其组成一个索引序列，利用它可以同时获得索引和值
        if item == key:                           #enumerate在字典上是枚举、列举的意思
            return index
    return -1

    #return 0：一般用在主函数结束时，按照程序开发的一般惯例，表示成功完成本函数。
    #return -1：:表示返回一个代数值，一般用在子函数结尾。按照程序开发的一般惯例，表示该函数失败；
    #return  1 ：表示非正常终止，函数被不确定原因终止了

    '''

    def bin_search(items, key):
        """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

    '''