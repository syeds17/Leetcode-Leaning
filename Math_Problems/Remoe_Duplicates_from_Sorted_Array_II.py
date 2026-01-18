"""
Problem: Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Approach:
- Use two pointers to modify the array in-place
- Allow at most two occurrences of each element
- Compare current element with the element two positions before

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        i = 2
        for j in range(2,n):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i        
