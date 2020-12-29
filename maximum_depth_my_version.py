# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global_count = 0
    def find_max_depth(self, root, current_depth):
        if(root == None):
            return
        if(current_depth > self.global_count):
            self.global_count = current_depth
        self.find_max_depth(root.left, current_depth + 1)
        self.find_max_depth(root.right, current_depth + 1)
        
    def maxDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        self.find_max_depth(root, 1)
        
        return self.global_count
        
