class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        for num in nums: 
            if num in seen: 
                return True 
            seen.add(num)
        return False
# Time complexity: O(n^2)
# loop through the array first 
# loop through the array starting from index i 

# use sorting 
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False
# Time Complexity: O(nlogn) 
# Space Complexity: O(n) 

# use HashSet
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
# Time Complexity: O(n)
# Space Complexity: O(n) 