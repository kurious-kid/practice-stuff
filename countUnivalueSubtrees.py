# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    countOfNodes = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        self.countOfNodes = 0
        self.getCountUnivalSubtrees(root, root.val)
        return self.countOfNodes

    def getCountUnivalSubtrees(self, node, parentValue) -> bool:
        if (node == None):
            return True
        elif (node.right == None and node.left == None):
            self.countOfNodes += 1
            if (node.val == parentValue):
                return True
            else:
                return False
        else:
            leftHalf = self.getCountUnivalSubtrees(node.left, node.val)
            rightHalf = self.getCountUnivalSubtrees(node.right, node.val)
            if (leftHalf and rightHalf):
                self.countOfNodes += 1
                return True