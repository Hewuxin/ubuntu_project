def maopao_sort(alist):
    """
    时间复杂度O(n^2)
    空间复杂度O(n)
    :param alist:
    :return:
    """
    for i in range(len(alist)-1):
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


def chosen_sort(alist):
    """
    时间复杂度O(n^2)
    空间复杂度O(n)
    稳定性 不稳定
    :param alist:
    :return:
    """

    for i in range(len(alist)-1):
        mid = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[mid]:
                mid = j
        alist[i], alist[mid] = alist[mid], alist[i]

    return alist


def insert_sort(alist):
    """
    时间复杂度O(n^2)
    稳定性: 稳定
    :param alist:
    :return:
    """

    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist


def merge_sort(alist):
    if len(alist) < 2:
        return alist
    n = len(alist) // 2
    left = merge_sort(alist[:n])
    right = merge_sort(alist[n:])

    return merge(left, right)


def merge(left, right):
    """
    时间复杂度O(nlogn)
    稳定性稳定
    :param left:
    :param right:
    :return:
    """
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


def shell_sort(alist):
    if alist < 2:
        return alist
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            j = i
            while j < gap:
                if alist[gap-j] > alist[gap+j]:
                    alist[gap-j], alist[gap+j] = alist[gap+j], alist[gap-j]
                    j -= 1
        gap = gap // 2
