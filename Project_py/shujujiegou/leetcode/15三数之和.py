"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组
"""


def threeSum(nums):
    """
    时间复杂度 O(N**2)
    空间复杂度 O(1)
    :param nums:
    :return:
    """
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0:  # 最小数大于0
            break

        if k > 0 and nums[k] == nums[k - 1]:
            continue
        i, j = k + 1, len(nums) - 1

        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1

            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1

                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res


if __name__ == "__main__":
    threeSum([-1,0,1,2,-1,-4])

