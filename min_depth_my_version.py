# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def helper_function(self, root, depth_so_far, the_list_of_depths):
        if(root == None):
            return 
        else:
            if(root.left == None and root.right == None):
                the_list_of_depths.append(depth_so_far)
                
            self.helper_function(root.left, depth_so_far + 1, the_list_of_depths)
            self.helper_function(root.right, depth_so_far + 1, the_list_of_depths)
            # if(left != -1 and right != -1):
            #     return min(left, right) + 1
            # elif(left != -1 and right == -1):
            #     return left
            # elif(left == -1 and right != -1):
            #     return right 
            # elif(left == -1 and right == -1):
            #     return 1
                    
        
    def minDepth(self, root: TreeNode) -> int:
        the_list_of_depths = []
        if(root == None):
            return 0
        self.helper_function(root, 1, the_list_of_depths)
        # to_return = min(the_list_of_depths)
        # self.the_list_of_depths = []
        return min(the_list_of_depths)
        
