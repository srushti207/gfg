#User function Template for python3




# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        
        # code here
        if root is None:
            return []
        r = [root]
        result = []
        while(len(r)>0):
            result.append(r[0].data)
            nl = []
            for node in r:
                if node.right:
                    nl.append(node.right)
                if node.left:
                    nl.append(node.left)
            r = nl
        return result