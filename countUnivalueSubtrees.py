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
            return False

        self.countOfNodes = 0
        self.getCountUnivalSubtrees(root, root.val)
        return self.countOfNodes

    def getCountUnivalSubtrees(self, node, parentValue):
        if (node == None):
            return True
        elif (node.right == None and node.left == None):
            print("I am in a leaf node")
            self.countOfNodes += 1
            if (node.val == parentValue):
                return True
            else:
                return False
        else:
            if (self.getCountUnivalSubtrees(node.left, node.val) and self.getCountUnivalSubtrees(node.right, node.val)):
                self.countOfNodes += 1