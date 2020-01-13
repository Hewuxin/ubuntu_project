"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

"""

a = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


def searchMatrix(matrix, target):
    """
    时间复杂度O(m+n)
    :param matrix:
    :param target:
    :return:
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    height = len(matrix)   # 列长度
    width = len(matrix[0])  # 行长度

    col = 0
    row = height - 1

    while col < width and row >= 0:
        # 从左下角开始移动 上下移动
        if matrix[row][col] > target:
            row -= 1
            # 左右移动
        elif matrix[row][col] < target:
            col += 1
        else:
            return True
    return False


print(searchMatrix(a, 17))
