# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    count_of_paths = 0
    original_sum = 0
    
    def solve_path_sum_3(self, root, sum):
        if(root == None):
            return
        elif((sum - root.val) == 0):
            self.count_of_paths += 1
            self.solve_path_sum_3(root.left, self.original_sum)
            self.solve_path_sum_3(root.right, self.original_sum)
            
        else:
            self.solve_path_sum_3(root.left, sum - root.val)
            self.solve_path_sum_3(root.right, sum - root.val)
            self.solve_path_sum_3(root.left, sum)
            self.solve_path_sum_3(root.right, sum)
        
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.original_sum = sum
        if(root == None):
            return 0
        else:
            self.solve_path_sum_3(root, sum)
            
        return self.count_of_paths
