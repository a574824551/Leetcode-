class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i
