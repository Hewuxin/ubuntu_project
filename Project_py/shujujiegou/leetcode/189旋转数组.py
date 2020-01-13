"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""


def rotate(alist, k):
    num = len(alist)
    b = list(range(num))
    for i in range(num):
        b[(i+k) % num] = alist[i]
    a[::] = b[::]


def rotate1(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]


def rotate2(nums, k):
    k %= len(nums)

    nums = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]


def rotate3(nums, k):
    k %= len(nums)

    for _ in range(k):
        nums.insert(0, nums.pop())


a = [1, 2, 3, 4, 5, 6, 7]
# rotate(a, 3)
rotate1(a, 3)
print(a)


