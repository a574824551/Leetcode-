class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(len (substr) for substr in ''.join([str(x) for x in nums]).split("0"))
