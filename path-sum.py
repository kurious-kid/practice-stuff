# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(root == None):
            return False
        elif((sum - root.val) == 0 and (root.left == None) and (root.right == None)):
            return True
        else:
            left = self.hasPathSum(root.left, sum - root.val)
            right = self.hasPathSum(root.right, sum - root.val)

            return (left or right)
            
