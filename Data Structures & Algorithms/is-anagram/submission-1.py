#  use sorting algorithm
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t): return False 
#         return sorted(s) == sorted(t)

# Time complexity: O(nlogn)   
# sorted can be used for any types that can compare with each other 
# strings / tuples/ dictionaries 
        
# they need to share the same length 
# they need to share the same lists of characters included in the string as well 


# solution 2: can think about hash map 
class Solution: 
    def isAnagram(self, s:str, t:str) -> bool: 
        if len(s) != len(t): return False 
        countS, countT = {}, {} #create frequency dictionaries 
        for i in range (len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)# increase the count of this character by 1
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # key idea: if the charactere is found, coutn if not return 0 
        return countS == countT
