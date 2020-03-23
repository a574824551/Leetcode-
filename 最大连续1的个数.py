class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(len (substr) for substr in ''.join([str(x) for x in nums]).split("0"))
        #转为字符串，以0为分隔符得到list，求元素中最长长度。
