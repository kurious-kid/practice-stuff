# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def do_inorder_traversal(self, root, the_list):
        if(root != None):
            self.do_inorder_traversal(root.left, the_list)
            the_list.append(root.val)
            self.do_inorder_traversal(root.right, the_list)
        
    def isValidBST(self, root: TreeNode) -> bool:
        the_list = []
        
        self.do_inorder_traversal(root, the_list)
        
        for i in range(1, len(the_list)):
            if(the_list[i] <= the_list[i - 1]):
                return False
            
        return True
        
        
