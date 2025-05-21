#User function Template for python3




class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def KDistance(self,root,k):
        res = []
        def dfs(node,count):
            if not node:
                return 
            if count == k:
                res.append(node.data)
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        dfs(root,0)
        return res
        
    