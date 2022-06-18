# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkIfHasSum(root, targetSum)

    def checkIfHasSum(self, root, targetSum):
        if (root == None):
            return False
        if (targetSum - root.val == 0 and (root.left == None and root.right == None)):
            return True
        else:
            return self.checkIfHasSum(root.right, targetSum - root.val) or self.checkIfHasSum(root.left,
                                                                                              targetSum - root.val)