
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        # Code here
        if not root:
            return []
        boundary = []
        if not self.is_leaf(root):
            boundary.append(root.data)
        self.left_boundary(root,boundary)
        self.leaves(root,boundary)
        self.right_boundary(root,boundary)
        return boundary
    
    def is_leaf(self,node):
        return node.left is None and node.right is None
        
    def left_boundary(self, node, boundary):
        curr = node.left
        while curr:
            if not self.is_leaf(curr):
                boundary.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
                
    def leaves(self,node,boundary):
        if node is None:
            return
        if self.is_leaf(node):
            boundary.append(node.data)
        self.leaves(node.left, boundary)
        self.leaves(node.right,boundary)
        
    def right_boundary(self,node,boundary):
        curr = node.right
        stack = []
        while curr:
            if not self.is_leaf(curr):
                stack.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        while stack:
            boundary.append(stack.pop())
            
        
        
            