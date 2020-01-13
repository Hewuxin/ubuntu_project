def sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
#  时间复杂度 O(n**2)
#  稳定性 稳定


if __name__ == "__main__":
    print(sort([1, 2, 5, 4, 3, 10, 6, 15, 9]))
