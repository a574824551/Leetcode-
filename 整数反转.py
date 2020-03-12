class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=-1*int(str(-1*x)[::-1])
        if abs(x)>2147483647:return 0
        return x
