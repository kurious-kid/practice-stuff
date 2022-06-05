# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        self.answer = 0
        self.calculateMaxDepth(root, 1)
        return self.answer

    def calculateMaxDepth(self, node, depth):
        if (node == None):
            self.answer = max(self.answer, depth - 1)
            return
        self.calculateMaxDepth(node.left, depth + 1)
        self.calculateMaxDepth(node.right, depth + 1)
