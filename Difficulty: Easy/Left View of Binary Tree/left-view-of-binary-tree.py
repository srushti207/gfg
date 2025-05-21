#User function Template for python3



# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        # code here
        if root is None:
            return []
        l = [root]
        result = []
        while(len(l)>0):
            result.append(l[0].data)
            nl = []
            for node in l:
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)
            l = nl
        return result
            