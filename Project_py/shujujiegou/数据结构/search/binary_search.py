"""
必须是有序顺序表
时间复杂度O(logn)
空间复杂度O(1)
"""


def binary_search(alsit, item):
    """递归查找"""
    n = len(alsit)
    if n > 0:
        mid = n // 2
        if item == alsit[mid]:
            return True
        elif item < alsit[mid]:
            return binary_search(alsit[:mid], item)
        else:
            return binary_search(alsit[mid+1:], item)
    return False


def binary_search01(alist, item):
    n = len(alist)-1
    first = 0
    last = n
    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    list03 = [1, 4, 5, 6, 10, 15, 12, 55, 99, 100]
    print(binary_search(list03, 5))
    print(binary_search(list03, 50))
    print(binary_search01(list03, 50))
    print(binary_search01(list03, 5))
