"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

"""


class Solution:
    def searchRage(self, nums, target):
        """
        二分查找
        时间复杂度 O(logn)
        :param nums:
        :param target:
        :return:
        """
        #  target起始位置查找
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if not nums or nums[l] != target:
            return [-1, -1]
        #  target 结束位置查找
        a, b = l, len(nums) - 1

        while a < b:
            mid = (a + b + 1) // 2
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1

        return [l, a]
