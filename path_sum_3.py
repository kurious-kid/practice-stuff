# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy

class Solution:
    
    count_of_paths = 0
    original_sum = 0
    
    def solve_path_sum_3(self, root, sum, path_so_far):
        if(root == None):
            return
        elif((sum - root.val) == 0):
            self.count_of_paths += 1
            path_so_far.append(root.val)
            print("path so far for this addition: ", path_so_far)
            # left_side = []
            # right_side = []
            # self.solve_path_sum_3(root.left, self.original_sum, left_side)
            # self.solve_path_sum_3(root.right, self.original_sum, right_side)
            
        else:
            left_with_inclusion = copy.deepcopy(path_so_far)
            left_with_inclusion.append(root.val)
            self.solve_path_sum_3(root.left, sum - root.val, left_with_inclusion)
            
            right_with_inclusion = copy.deepcopy(path_so_far)
            right_with_inclusion.append(root.val)
            self.solve_path_sum_3(root.right, sum - root.val, right_with_inclusion)
            
            left_without_inclusion = []
            right_without_inclusion = []
            
            self.solve_path_sum_3(root.left, self.original_sum, left_without_inclusion)
            self.solve_path_sum_3(root.right, self.original_sum, right_without_inclusion)
        
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.original_sum = sum
        path_so_far = []
        if(root == None):
            return 0
        else:
            self.solve_path_sum_3(root, sum, path_so_far)
            
        return self.count_of_paths
        
        
