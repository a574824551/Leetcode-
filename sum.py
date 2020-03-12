class Solution(object):
    def twoSum(self,nums, target):
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i,hashmap.get(target - num)]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                #if nums[i]>target or nums[j]>target:
                #    continue
                if nums[i]+nums[j]==target:
                    return [i,j]
        '''
