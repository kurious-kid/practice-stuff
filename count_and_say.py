class Solution:
    def get_groups(self, the_string):
        the_groups = []
        current_count = 1
        for i in range(1, len(the_string)):
            if(the_string[i] == the_string[i-1]):
                current_count += 1
            else:
                the_groups.append(str(current_count))
                the_groups.append(the_string[i-1])
                current_count = 1
                
        the_groups.append(str(current_count))
        the_groups.append(the_string[len(the_string) - 1])
        
        the_call = ''
        for each_element in the_groups:
            the_call = the_call + each_element
        
        return the_call
        
            
            
    def countAndSay(self, n: int) -> str:
        the_dict = [-1] * 31
        the_dict[1] = str(1)
        
        for i in range(2, n + 1):
            the_dict[i] = self.get_groups(the_dict[i - 1])
            # print("the_dict[str(i)]: ",the_dict[i])
               
        return the_dict[n]
        
        
        
