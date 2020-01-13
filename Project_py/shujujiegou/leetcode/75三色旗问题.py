"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""


class Solution:
    def sortColors(self, nums):
        """
        时间复杂度O(n)
        空间复杂度O(1)
        :param nums:
        :return:
        三色旗问题，最初可将其看为四类：red，white，blue和unclassified
           |——0——|--1---|--unclassified--|--2---|
                 |      |                |
                red   white             blue
           当white与blue未重合时：
               如果nums[w]为0，则交换放到red区间，red和white都加1。
               如果nums[w]为1，则white指针加1。
               如果nums[w]为2，则交换放到 blue 区间，blue减1。
        """
        r, w, b = 0, 0, len(nums)-1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
