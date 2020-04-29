class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return False
        i=1
        while(i!=len(nums)):
            if nums[i]==nums[i-1]:
                del nums[i-1]
            else:
                i=i+1
        return i
