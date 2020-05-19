class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        if len(nums1)<=len(nums2):
            dict1={}
            for x in nums1:#统计较短list元素个数
                if x in dict1:
                    dict1[x]+=1
                else:
                    dict1[x]=1
            for x in nums2:
                if x in dict1:
                    if dict1[x]>0:
                        dict1[x]-=1
                        res.append(x)
        else:
            dict1={}
            for x in nums2:#统计较短list元素个数
                if x in dict1:
                    dict1[x]+=1
                else:
                    dict1[x]=1
            for x in nums1:
                if x in dict1:
                    if dict1[x]>0:
                        dict1[x]-=1
                        res.append(x)
        return res
