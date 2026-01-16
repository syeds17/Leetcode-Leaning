"""
Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Approach:
- Use two pointers: one for iterating through the array, one for tracking the position to place non-zero elements
- Traverse the array once
- Move all non-zero elements to the front while maintaining their relative order
- Fill the remaining positions with zeros

Time Complexity: O(n)
Space Complexity: O(1)  # in-place modification
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range (0,n):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j += 1
