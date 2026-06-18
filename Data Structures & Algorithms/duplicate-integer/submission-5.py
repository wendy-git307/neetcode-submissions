class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)): 
            if nums[i] in seen:
                return True 
            seen.add(nums[i]) # set does not have attribute append but have attribute add and remove 
        return False 