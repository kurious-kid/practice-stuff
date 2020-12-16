# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if(len(nums) == 1):
            curr_node = TreeNode()
            curr_node.val = nums[0]
            return curr_node
        
        elif(len(nums) == 0):
            return None
        
        else:
            index_of_largest = nums.index(max(nums))
            curr_node = TreeNode()
            curr_node.val = nums[index_of_largest]
            curr_node.left = self.constructMaximumBinaryTree(nums[0:index_of_largest])
            curr_node.right = self.constructMaximumBinaryTree(nums[index_of_largest + 1 : len(nums)])
            return curr_node
        
