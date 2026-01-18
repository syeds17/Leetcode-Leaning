"""
Problem: Sort Colors
Link: https://leetcode.com/problems/sort-colors/

Approach:
- Use three pointers: low, mid, and high
- Place 0s to the left, 2s to the right, and 1s in the middle
- Swap elements accordingly while traversing the array

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first = 0
        mid = 0
        last = n-1
        while mid<=last:
            if nums[mid]==0:
                nums[first],nums[mid]=nums[mid],nums[first]
                first += 1
                mid += 1
            elif nums[mid]==1:
                mid += 1
            else:
                nums[mid],nums[last]=nums[last],nums[mid]
                last -= 1    
