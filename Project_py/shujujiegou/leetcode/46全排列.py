"""
    给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums):
        def backtrack(nums, tmp):
            if nums == []:
                if tmp not in res:
                    res.append(tmp[::])

            else:
                for i in range(len(nums)):
                    tmp.append(nums[i])
                    backtrack(nums[0:i] + nums[i+1:], tmp)

            if tmp == []:
                return
            tmp.pop()

        res = []
        tmp = []
        backtrack(nums, tmp)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))

