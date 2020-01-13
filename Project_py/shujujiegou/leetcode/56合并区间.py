"""
给出一个区间的集合，请合并所有重叠的区间。
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
import time


class Solution:
    """
    时间复杂度n^2
    空间复杂度O(n)
    """
    def merge(self, intervals):
        intervals = sorted(intervals)
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            while i < n - 1 and intervals[i+1][0] <= right:
                i += 1
                right = max(intervals[i][1], right)
            res.append([left, right])
            i += 1

        return res


if __name__ == "__main__":
    a = [[1, 4], [4, 5]]
    b = [[1, 2], [2, 6], [8, 10], [15, 18]]
    print(time.clock())
    s = Solution()
    print(s.merge(a))
    print(time.clock())
    print(s.merge(b))


