class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        %字母异位词可以理解为两个词的字母组成相同，对s构建词表计数器，遍历t时减去看是否全部归零是正常思路，这里偷鸡了一波
