class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            find = target-nums[i]
            if find in nums[i+1:]:
                f=nums[i+1:].index(find)
                return [i,i+1+f]
