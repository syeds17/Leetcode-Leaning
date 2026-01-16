"""
Problem: Find All Numbers Disappeared in an Array
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Approach:
- Iterate through the array and mark the presence of numbers by negating the value at corresponding indices
- After marking, the indices with positive values indicate missing numbers
- Collect these indices as the result

Time Complexity: O(n)
Space Complexity: O(1)  # ignoring output array
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            index = abs(num)-1
            nums[index] = -abs(nums[index])
        uniq = []
        for i in range (len(nums)):
            if nums[i]>0:
                uniq.append(i+1)
        return uniq         
                
        
