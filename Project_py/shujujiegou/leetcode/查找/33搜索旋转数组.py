"""
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
直接使用二分法，判断那个二分点,有几种可能性
直接等于target
在左半边的递增区域
    a. target 在 left 和 mid 之间
    b. 不在之间
在右半边的递增区域
    a. target 在 mid 和 right 之间
    b. 不在之间
相关题目: 81. 搜索旋转排序数组 II

"""


class Solution:
    def search(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n - 1
# [4,5,6,7,0,1,2] 0  l = 0 r = 6
        while left < right:
            mid = left + (right - left) // 2  # 3
            if nums[mid] == target:    # 7
                return mid

            elif nums[left] < nums[mid]:  # 4  7
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums[left] == target else -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 10))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 2))
