class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for each_row in matrix:
            if(len(each_row) == 0):
                return False
            if(target > each_row[len(each_row) - 1]):
                continue
            else:
                for each_element in each_row:
                    if(each_element == target):
                        return True
                    
        return False
