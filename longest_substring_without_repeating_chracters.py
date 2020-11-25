class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        the_map = []
        current_longest = 1
        for i in range(len(s)):
            the_map.append(s[i])
            temp = 1
            for j in range(i + 1, len(s)):
                if (s[j] not in the_map):
                    temp += 1
                    the_map.append(s[j])
                else:
                    break
            if temp >= current_longest:                        
                current_longest = temp
            the_map = []
                    
                    
        return current_longest
                
