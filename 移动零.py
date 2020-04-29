class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow=0
        for quick in range(len(nums)):
            if nums[quick]!=0:
                tmp=nums[quick]
                nums[quick]=0
                nums[slow]=tmp
                slow+=1
            quick+=1
