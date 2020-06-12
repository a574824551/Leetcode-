class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='1'
        num=1
        
        if n==1:return s
        
        while(True):
            num+=1
            #生成当前行的s
            cur=s[0]
            count=0
            new_s=''
            l=0
            while(l!=len(s)):
                if s[l]==cur:
                    count+=1
                    l+=1
                else:
                    new_s=new_s+str(count)+str(cur)
                    cur=s[l]
                    count=0
            if count!=0:
                s=new_s+str(count)+str(cur)
            else:s=new_s
                
            if n==num:return s
