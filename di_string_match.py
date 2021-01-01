class Solution:
    def diStringMatch(self, S: str) -> List[int]: 
        i_beginning = 0
        d_beginning = len(S)
        the_output = []
        for each_character in S:
            if(each_character == "I"):
                the_output.append(i_beginning)
                i_beginning += 1
                
            else:
                the_output.append(d_beginning)
                d_beginning -= 1
                
        the_output.append(i_beginning)
        
        return the_output
