class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        return sorted(s) == sorted(t)
        
        
# they need to share the same length 
# they need to share the same lists of characters included in the string as well 
# use sorted