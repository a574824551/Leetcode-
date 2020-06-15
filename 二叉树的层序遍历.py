# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:return []
        
        queue=[(root,0)]
        index=0
        res = collections.defaultdict(list)
        while index<len(queue):
            cur=queue[index]
            res[cur[1]].append(cur[0].val)
            if cur[0].left:
                queue.append((cur[0].left,cur[1]+1))
            if cur[0].right:
                queue.append((cur[0].right,cur[1]+1))
            index+=1

        return res.values()
