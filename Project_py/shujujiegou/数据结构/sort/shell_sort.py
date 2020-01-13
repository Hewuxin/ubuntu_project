def shell_sort(nums):
    """
    时间复杂度 O(n**1.3)
    最差时间复杂度O(n**2)
    稳定性 不稳定  会改变相同元素间的相对顺序
    :param nums:
    :return:
    """
    n = len(nums)
    gap = n // 2

    while gap >= 1:  # 缩短步长
        for i in range(gap, n):  # 遍历当前子序列的所有元素
            j = i
            while j > 0:  # 每一个子序列执行插入排序
                if nums[j] < nums[j-gap]:
                    nums[j], nums[j-gap] = nums[j-gap], nums[j]
                    j -= gap
                else:
                    break
        gap = gap // 2   # 缩短步长
    return nums

# 时间复杂度 O(n^2) 最好时间复杂度O(n^1.3)
#  稳定性 不稳定  相同元素的相对顺序会发生改变


if __name__ == "__main__":
    print([1, 8, 4, 5, 7, 6, 10, 15, 12])
    print(shell_sort([1, 8, 4, 5, 7, 6, 10, 15, 12]))
