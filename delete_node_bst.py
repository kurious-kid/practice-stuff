# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find_the_node(self, root, key):
        while(1):
            if(root == None):
                return None
            elif(key < root.val):
                root = root.left
            elif(key > root.val):
                root = root.right
            elif(key == root.val):
                return root
                
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        temp = root
        search_result = self.find_the_node(root, key)
        
        if(search_result == None):
            return temp
        else:
            
        
