import math
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0] == 1):
            return -1
        the_queue = []
        the_queue.append((0,0,1))
        target_reached = False
        target_i = len(grid) - 1
        target_j = len(grid) - 1
        dimension_of_grid = len(grid) - 1
        visited = {}
        current_best = math.inf
        for i in range(dimension_of_grid + 1):
            for j in range(dimension_of_grid + 1):
                visited[(i,j)] = math.inf
                
        visited[(0,0)] = True
        
        while(len(the_queue) > 0):
            current_node = the_queue.pop()
            current_i = current_node[0]
            current_j = current_node[1]
            current_path_length = current_node[2]
            # print("current_i: ", current_i)
            # print("current_j: ", current_j)
            if(current_i == target_i and current_j == target_j):
                if(current_path_length < current_best):
                    current_best = current_path_length
                    target_reached = True
                # return current_path_length
            
            if((0 <= current_i+1 <= dimension_of_grid) and (0 <= current_j+1 <= dimension_of_grid) and grid[current_i+1][current_j+1] == 0 and visited[(current_i+1, current_j + 1)] > current_path_length + 1):
                        visited[(current_i+1, current_j + 1)] = current_path_length + 1
                        the_queue.append((current_i+1, current_j+1, current_path_length + 1))
                        
            if((0 <= current_i - 1 <= dimension_of_grid) and (0 <= current_j <= dimension_of_grid) and grid[current_i-1][current_j] == 0 and visited[(current_i - 1, current_j)] > current_path_length + 1):
                
                visited[(current_i - 1, current_j)] = current_path_length + 1
                the_queue.append((current_i - 1, current_j, current_path_length + 1))
                        
            if((0 <= current_i-1 <= dimension_of_grid) and (0 <= current_j+1 <= dimension_of_grid) and grid[current_i-1][current_j+1] == 0 and visited[(current_i - 1, current_j + 1)] > current_path_length + 1):
                        visited[(current_i - 1, current_j + 1)] = current_path_length + 1
                        the_queue.append((current_i - 1, current_j+1, current_path_length + 1))
                                   
            if((0 <= current_i <= dimension_of_grid) and (0 <= current_j+1 <= dimension_of_grid) and grid[current_i][current_j+1] == 0 and visited[(current_i, current_j + 1)] > current_path_length + 1):
                        visited[(current_i, current_j + 1)] = current_path_length + 1
                        the_queue.append((current_i, current_j + 1, current_path_length + 1))
                        
            if((0 <= current_i+1 <= dimension_of_grid) and (0 <= current_j <= dimension_of_grid) and grid[current_i+1][current_j] == 0 and visited[(current_i+1, current_j)] > current_path_length + 1):
                        visited[(current_i+1, current_j)] = current_path_length + 1
                        the_queue.append((current_i +1, current_j, current_path_length + 1))
                        
            if((0 <= current_i+1 <= dimension_of_grid) and (0 <= current_j-1 <= dimension_of_grid) and grid[current_i+1][current_j-1] == 0 and visited[(current_i+1, current_j-1)] > current_path_length + 1):
                        visited[(current_i+1, current_j-1)] = current_path_length + 1
                        the_queue.append((current_i+1, current_j-1, current_path_length + 1))
                        
            if((0 <= current_i <= dimension_of_grid) and (0 <= current_j-1 <= dimension_of_grid) and grid[current_i][current_j-1] == 0 and visited[(current_i, current_j-1)] > current_path_length + 1):
                        visited[(current_i, current_j-1)] = current_path_length + 1
                        the_queue.append((current_i, current_j-1, current_path_length + 1))
            if((0 <= current_i-1 <= dimension_of_grid) and (0 <= current_j-1 <= dimension_of_grid) and grid[current_i-1][current_j-1] == 0 and visited[(current_i-1, current_j-1)] > current_path_length + 1):
                        visited[(current_i-1, current_j-1)] = current_path_length + 1
                        the_queue.append((current_i - 1, current_j-1, current_path_length + 1))
                
        if(target_reached):
            return current_best
        return -1
            
            
                
        
