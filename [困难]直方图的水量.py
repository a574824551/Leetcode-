class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h_left=[]
        h_cur=0
        for i in height:
            if i>h_cur:
                h_left.append(h_cur)
                h_cur=i
            else:
                h_left.append(h_cur)
        print h_left
        h_right=[]
        h_cur=0
        for i in height[::-1]:
            if i>h_cur:
                h_right.append(h_cur)
                h_cur=i
            else:
                h_right.append(h_cur)
        h_right=h_right[::-1]
        output=[]
        for i in range(len(h_left)):
            water=min(h_left[i],h_right[i])-height[i]
            if water<0:
                water=0
            output.append(water)
        return sum(output)
