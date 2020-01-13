"""
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞

"""


def search(nums):
    """
    时间复杂度 O(n)
    空间复杂度O(1)
    :param nums:
    :return:
    """
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums) - 1


def findPeekelement(nums, l, r):

    if l == r:
        return l
    mid = (l+r) // 2
    if nums[mid] > nums[mid+1]:
        return findPeekelement(nums, l, mid)
    else:
        return findPeekelement(nums, mid+1, r)


def findPeekElement(nums, l, r):
    """
    迭代 时间复杂度O(logn)
    二分查找

    :param nums:
    :param l:
    :param r:
    :return:
    """
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid + 1
    return l