"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
"""


def help_(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return help_(x*x, n / 2)
    return help_(x*x, (n-1) / 2) * x


def pow_(x: float, n: int) -> float:
    if n < 0:
        n = -n
        return 1 / help_(x, n)


def pow_01(x: float, n: int) -> float:
    judge = True
    if n < 0:
        n = -n
        judge = False

    final = 1
    while n > 0:
        if n %2 == 0:
            x *= x
            n //= 2
        final *= x
        n = n -1
    return final if judge else 1/final
