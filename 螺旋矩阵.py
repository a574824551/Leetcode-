class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r, i, j, di, dj = [], 0, 0, 0, 1#结果，当前横纵坐标，横纵坐标变化方向
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = 0#走过的位置设为0，若矩阵有0元素可改为None
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:#若下一步已走过，改变反向
                    di, dj = dj, -di
                i += di
                j += dj
        return r

        #参考了评论区Tokisaki Kurumi的代码
