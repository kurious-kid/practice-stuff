# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        output = []
        
        self.do_post_order_traversal(root, output)
        
        return output
    
    def do_post_order_traversal(self, root, output):
        if(root):
            self.do_post_order_traversal(root.left, output)
            self.do_post_order_traversal(root.right, output)
            output.append(root.val)
        
