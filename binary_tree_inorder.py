# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.do_inorder_traversal(root, output)
        
        return output
    
    def do_inorder_traversal(self, root, output):
        if(root):
            self.do_inorder_traversal(root.left, output)
            output.append(root.val)
            self.do_inorder_traversal(root.right, output)
        
