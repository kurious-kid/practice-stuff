# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy

class Solution:
    
    
    def get_paths_recursively(self, root, sum, path_so_far, list_to_be_returned):
        if(root == None):
            return
        elif((sum - root.val == 0) and (root.left == None) and (root.right == None)):
            path_so_far.append(root.val)
            list_to_be_returned.append(path_so_far)
            return
        else:
            left_path = copy.deepcopy(path_so_far)
            left_path.append(root.val)
            self.get_paths_recursively(root.left, sum - root.val, left_path, list_to_be_returned)
            
            right_path = copy.deepcopy(path_so_far)
            right_path.append(root.val)
            self.get_paths_recursively(root.right, sum - root.val, right_path, list_to_be_returned)
        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path_so_far = []
        list_to_be_returned = []
        if(root == None):
            return list_to_be_returned
        self.get_paths_recursively(root, sum, path_so_far, list_to_be_returned)
        
        return list_to_be_returned
        
