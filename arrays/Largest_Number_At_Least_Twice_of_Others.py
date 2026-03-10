"""
Problem: Largest Number At Least Twice of Others
Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/

Approach:
- Find the largest number and its index
- Check if the largest number is at least twice every other number
- If the condition holds, return the index of the largest number
- Otherwise, return -1

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_index = nums.index(max_val)
        for num in nums:
            if max_val != num and max_val < 2*num:
                return -1
        return max_index    
            
            
