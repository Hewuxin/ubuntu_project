def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums
# 时间复杂度 最好O(n) 最差 O(n^2)
#  稳定性 稳定


if __name__ == "__main__":
    print(insert_sort([1, 2, 5, 4, 3, 10, 6, 15, 9]))
