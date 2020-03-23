class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if s > sum(nums):
            return 0
        
        left, right, res, sum_lr = 0, 0, len(nums)+1, 0
        
        for right in range(len(nums)):
            sum_lr += nums[right]
            while sum_lr >= s:
                res = min(res, right - left + 1)
                sum_lr -= nums[left]
                left += 1
        return res
