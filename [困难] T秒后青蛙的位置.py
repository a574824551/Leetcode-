class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        dian={}
        father=[1]*n
        son=[0]*n
        for [a,b] in edges:
            if a>b:
                tmp=a
                a=b
                b=tmp
            if a in dian:
                dian[a]+=1
            else:
                dian[a]=1
            father[b-1]=a
            son[a-1]+=1

        path=[target]
        cur=target

        while cur!=1:
            path.append(father[cur-1])
            cur = father[cur-1]
  
        if t<len(path)-1:return 0
        if t>len(path)-1 and son[target-1]!=0:return 0

        path.reverse()

        prob=1
        for i in path:
            if i in dian:
                prob=prob* (1.0/dian[i])
        return prob
