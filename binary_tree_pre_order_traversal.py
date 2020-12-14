# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.do_pre_order_traversal(root, output)
        
        return output
        
    def do_pre_order_traversal(self,root, output):
        if(root):
            output.append(root.val)
            self.do_pre_order_traversal(root.left, output)
            self.do_pre_order_traversal(root.right, output)
