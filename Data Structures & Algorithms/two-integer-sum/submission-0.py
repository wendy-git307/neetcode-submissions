class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [] # create an empty array to hold indices at the position that sum of two numbers = target k 
        for i in range (len(nums)): 
            for j in range (i+1, len(nums)): 
                if nums[i] + nums[j] == target: 
                    result = [i, j]
        return result
# Time Complexity: O(n^2)