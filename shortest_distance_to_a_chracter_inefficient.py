import math
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        distance_array = [ math.inf] * len(S)
        
        for i in range(len(S)):
            if(S[i] == C):
                for j in range(len(S)):
                    if(S[i] == S[j]):
                        distance_array[j] = 0
                        
                    elif(distance_array[j] > abs(i - j)):
                        distance_array[j] = abs(i - j)
                
            else:
                continue
                
        return distance_array
        
