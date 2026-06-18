
class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool: 
        # Use a set to track seen numbers efficiently
        seen = set(nums)
        if len(nums) > len(seen): 
            return True 
        return False 

# => since set has these features => no duplicates/unordered and unchangeable => so we can easily check it with the original length of list 
# use nested loop with time complexity up to O(n^2) => 
# so for each element, it need to loop again over the list 
