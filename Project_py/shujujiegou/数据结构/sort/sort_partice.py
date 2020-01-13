"""
quick_sort
时间复杂度 最优O(nlogn)最差O(n^2)稳定性不稳定
 相同元素的相对顺序会改变
"""


def quick_sort(alist, first, last):

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

    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


def shell_sort(alist):
    """
    减增量的插入排序
    时间复杂度 最差时间复杂度O(n^2) 最优O(n^1.3)
    稳定性 不稳定
    :param alist:
    :return:
    """
    if len(alist) < 2:
        return alist

    n = len(alist)
    gap = n // 2

    while gap >= 1:
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap = gap // 2
    return alist

def maopao_sort(alist):
    """
    时间复杂度 O(n^2) 最优时间复杂度O(n)
    稳定性 稳定
    :param alist:
    :return:
    """
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


def xuanze_sort(alist):
    """
    时间复杂度O(n^2)
    稳定性 不稳定
    :param alist:
    :return:
    """
    for i in range(len(alist)-1):
        mid = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[mid]:
                mid = j
        alist[mid], alist[i] = alist[i], alist[mid]
    return alist


def insert_sort(alsit):
    """
    时间复杂度O(n^2)
    稳定性 稳定
    :param alsit:
    :return:
    """
    n = len(alsit)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alsit[j] < alsit[j-1]:
                alsit[j], alsit[j-1] = alsit[j-1], alsit[j]
    return alsit


def merge_sort(alist):
    """
    时间复杂度 O(nlogn)
    稳定性 稳定
    :param alist:
    :return:
    """
    if len(alist) <= 1:
        return alist
    n = len(alist)
    mid = n // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])

    return res


if __name__ == "__main__":
   list01 = [1, 8, 4, 5, 7, 6, 10, 15, 12]
   list02 = [1, 8, 4, 5, 7, 6, 10, 15, 12]
   list03 = [1, 8, 4, 5, 7, 6, 10, 15, 12]
   print("maopao___", maopao_sort(list01))
   print("--------")
   print("xuanze___", xuanze_sort(list01))
   print("--------")
   print("insert___", insert_sort(list01))
   print("--------")
   print("merge___", merge_sort(list01))
   print("--------")
   shell_sort(list03)
   print("shell___", list03)
   print("--------")
   quick_sort(list02, 0, len(list02) - 1)
   print("quick_sort", list02)
