import math
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        distance_array = [ math.inf] * len(S)
        
        distance = -len(S)
        
        for i in range(len(S)):
            if(S[i] == C):
                distance = i
            distance_array[i] = i - distance
                
        # Backward pass
        
        for i in range(len(S)-1, -1, -1):
            # print("i: ", i)
            if(S[i] == C):
                distance = i
                
            distance_array[i] = min(distance_array[i], abs(i -distance))
            
        return distance_array
