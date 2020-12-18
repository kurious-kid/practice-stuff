class Solution:
    
    def do_dfs(self, result, the_dict, out, level, digits):
        if(level == len(digits)):
            result.append(out)
            return
        
        current_strings = the_dict[digits[level]]
        
        for each_element in current_strings:
            self.do_dfs(result, the_dict, out + each_element, level + 1, digits)
        
    def letterCombinations(self, digits: str) -> List[str]:
        
        if(digits == ""):
            return []
        result = []
        the_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        out=''
        level = 0
        
        self.do_dfs(result, the_dict, out, level, digits)
        return result
        
