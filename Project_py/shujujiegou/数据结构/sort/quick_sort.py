def quick_sort(alist, first, last):
    """
    最优时间复杂度O(nlogn)
    最差时间复杂度O(n^2)
    稳定性 不稳定
    :param alist:
    :param first:
    :param last:
    :return:
    """
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    #  退出循环后low==high
    alist[low] = mid_value
    # 对mid_value左边的序列进行快排
    quick_sort(alist, first, low-1)
    # 对mid_value 右边的序列进行快排
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    a = [1, 8, 4, 5, 7, 6, 10, 15, 12]
    quick_sort(a, 0, len(a)-1)
    print(a)
