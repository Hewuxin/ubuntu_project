def sort(nums):
    for i in range(len(nums)):
        mid = i
        for j in range(i, len(nums)):
            if nums[j] < nums[mid]:
                mid = j
        nums[mid], nums[i] = nums[i], nums[mid]
    return nums
#  时间复杂度O(n^2)
#  稳定性不稳定 (每次选择最大的情况)


if __name__ == "__main__":
    print(sort([1, 2, 5, 4, 3, 10, 6, 15, 9]))
