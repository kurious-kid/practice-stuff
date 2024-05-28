class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        theMap = {}
        
        for eachCharacter in s:
            if(eachCharacter not in theMap):
                theMap[eachCharacter] = [1]
            else:
                theMap[eachCharacter].append(theMap[eachCharacter].pop() + 1)
                
        for eachCharacter in t:
            if(eachCharacter not in theMap):
                return False
            elif(len(theMap[eachCharacter]) == 1):
                theMap[eachCharacter].append(1)
                
            else:
                theMap[eachCharacter].append(theMap[eachCharacter].pop() + 1)
                
        for eachKey in theMap:
            if(theMap[eachKey][0] != theMap[eachKey][1]):
                return False
                    
        return True
         
