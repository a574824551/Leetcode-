class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        for i in range(1, numRows, 1):
            tmp = []
            for j in range(i+1):
                if 1 <= j < i:
                    tmp.append(res[i-1][j-1] + res[i-1][j])
                else:
                    tmp.append(1)
            res.append(tmp)
        return res
