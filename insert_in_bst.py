# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        temp = root
        while(1):
            if(root == None):
                curr_node = TreeNode()
                curr_node.val = val
                return curr_node

            elif((val > root.val) and (root.right != None)):
                root = root.right

            elif((val < root.val) and (root.left != None)):
                root = root.left

            elif((val > root.val) and (root.right == None)):
                curr_node = TreeNode()
                root.right = curr_node
                root.right.val = val
                return temp

            elif((val < root.val) and (root.left == None)):
                curr_node = TreeNode()
                root.left = curr_node
                root.left.val = val
                return temp
        
