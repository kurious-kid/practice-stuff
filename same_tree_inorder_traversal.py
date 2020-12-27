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
            
        else:
            the_list.append(None)
            return
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_traversal = []
        q_traversal = []
        
        self.do_inorder_traversal(p, p_traversal)
        self.do_inorder_traversal(q, q_traversal)
        
        print("p_traversal:", p_traversal)
        print("q_traversal:", q_traversal)
        if(len(p_traversal) != len(q_traversal)):
            return False
        
        for i in range(len(p_traversal)):
            if(p_traversal[i] != q_traversal[i]):
                return False
            
        return True
