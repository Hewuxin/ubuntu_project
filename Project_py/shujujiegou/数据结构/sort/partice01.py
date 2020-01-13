def shell_sort(alist):
    """
    减增量的插入排序
    时间复杂度 最差时间复杂度O(n^2) 最优O(n^1.3)
    稳定性 不稳定
    :param alist:
    :return:
    """
    n = len(alist)
    gap = n // 2

    while gap >= 1:  # 缩短步长
        for i in range(gap, n):  # 遍历当前子序列的每个元素
            j = i
            while j > 0:  # 插入排序
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap = gap // 2    # 缩短步长


if __name__ == "__main__":
    list03 = [1, 8, 4, 5, 7, 6, 10, 15, 12]
    shell_sort(list03)
    print(list03)
    