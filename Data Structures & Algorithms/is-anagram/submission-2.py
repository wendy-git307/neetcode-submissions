class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        count = [0] * 26
        for i in range(len(s)): 
            count[ord(s[i])-ord('a')] +=1 
            count[ord(t[i]) - ord('a')] -=1 
        
        for val in count: 
            if val != 0: 
                return False 
        return True


# create a frequency array count of size 26 initialized to 0 
# iterate through both strings 
# increment the count at the index corresponding to s[i]
# decrement the count at the index corresponding to t[i]
# after processing both strings, scan through the count array: 
# if any value is not 0 return falses since the frequencies differ 
# if all values are 0 in the count array, return true since the strings are anagrams 