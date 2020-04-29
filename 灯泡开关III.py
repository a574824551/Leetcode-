class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        max_value=0
        count=0
        for i in range(len(light)):
            if light[i]>max_value:
                max_value=light[i]
            if max_value==i+1:
                count+=1
        return count
                    
