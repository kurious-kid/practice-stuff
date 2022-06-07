# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    listToTraverse = []

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (root.left == None and root.right == None):
            return True
        else:
            self.listToTraverse = []
            self.buildListToTraverse(root)

        print("listToTraverse: ", self.listToTraverse)
        return self.checkIfSymmetric()

    def checkIfSymmetric(self):
        for i in range(0, int(len(self.listToTraverse) / 2)):
            if (self.listToTraverse[i] != self.listToTraverse[len(self.listToTraverse) - 1 - i]):
                return False
        return True

    def buildListToTraverse(self, root):

        if (root == None):
            self.listToTraverse.append(None)
            return
        # Left
        self.buildListToTraverse(root.left)

        # Root
        self.listToTraverse.append(root.val)

        # Right
        self.buildListToTraverse(root.right)

