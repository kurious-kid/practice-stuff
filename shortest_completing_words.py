import math

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate_dict = {}
        small_a = ord('a')
        small_z = ord('z')
        
        cap_A = ord('A')
        cap_Z = ord('Z')
        
        shortest_length = math.inf
        first_index = None
        
        
        for each_element in licensePlate:
            current_element = None
            if((small_a <= ord(each_element) <= small_z) or (cap_A <= ord(each_element) <= cap_Z)):
                if(cap_A <= ord(each_element) <= cap_Z):
                    the_difference = ord(each_element) - cap_A
                    current_element = chr(small_a + the_difference)
                else:
                    current_element = each_element
                    
                
                
            if(current_element == None):
                continue
                
            if(current_element in license_plate_dict):
                license_plate_dict[current_element] += 1
                
            else:
                # if((small_a <= ord(each_element) <= small_z) or (cap_A <= ord(each_element) <= cap_Z)):
                license_plate_dict[current_element] = 1
                    
        # print("printing license plate dict:", license_plate_dict)
                    
        for i in range(len(words)):
            temp_dict = {}
            word_length = 0
            flag = True
            for each_character in words[i]:
                word_length += 1
                if(each_character in temp_dict):
                    temp_dict[each_character] += 1
                else:
                    temp_dict[each_character] = 1
                    
            # print("prinitng temp dict: ", temp_dict)
            
            for each_key in license_plate_dict:
                if((each_key not in temp_dict)  or (temp_dict[each_key] < license_plate_dict[each_key])):
                    flag = False
                    continue
            
            if(word_length < shortest_length and flag):
                # print("in shortest word length if")
                # print("i:", i)
                shortest_length = word_length
                first_index = i
                
        # if(first_index == None):
        #     return 0
        
        return words[first_index]
            
        
        
