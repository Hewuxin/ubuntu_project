"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
"""


class Solution:
    """ 时间复杂度 O("""
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        s = 1 if dividend ^ divisor > 0 else -1   # 异或
        divd = abs(dividend)
        divr = abs(divisor)
        while divd >= divr:
            count += 1
            divd -= divr
        if s > 0 and (-2**31 < count < 2**31 - 1):
            return count
        elif s < 0 and -2**31 < count < 2**31 - 1:
            return 0 - count
        else:
            return 2**31-1


if __name__ == "__main__":
    s = Solution()
    print(s.divide(10, 3))  # 3
    print(s.divide(10, 2))  # 5
    print(s.divide(10, 4))  # 2
    print(s.divide(13, 2))  # 6
    print(s.divide(14, 5))  # 2
    print(s.divide(19, 3))  # 6
    print(s.divide(-19, 3))  # -6
    print(s.divide(19, -3))  # -6



