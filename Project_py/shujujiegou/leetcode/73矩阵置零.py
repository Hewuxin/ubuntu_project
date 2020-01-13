"""
给定一个 m x n 的矩阵，如果一个元素为 0，
则将其所在行和列的所有元素都设为 0。请使用原地算法。
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

"""


class Solution:
    def setZeros(self, matrix):
        """
        时间复杂度 O(m x n)
        空间复杂度O(m+n)
        :param matrix:
        :return:
        """
        n = len(matrix)
        m = len(matrix[0])
        row, col = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j] = 0

    def setZeros01(self, matrix):
        """
        时间复杂度O(m x n)
        空间复杂度O(1)
        :param matrix:
        :return:
        """
        r = len(matrix)
        c = len(matrix[0])
        row0_flag = False
        col0_flag = False

        # 判断第一列是否有0
        for i in range(r):
            if matrix[r][0] == 0:
                col0_flag = True
                break

        # 判断第一行是否有0
        for j in range(c):
            if matrix[0][c] == 0:
                row0_flag = True
                break

        for x in range(1, r):
            for y in range(1, c):
                if matrix[x][y] == 0:
                    matrix[x][0] = matrix[0][y] = 0

        for a in range(1, r):
            for b in range(1, r):
                if matrix[a][0] == 0 or matrix[0][b] == 0:
                    matrix[a][b] = 0

        if row0_flag:
            for i in range(c):
                matrix[0][i] = 0

        if col0_flag:
            for j in range(r):
                matrix[j][0] = 0
