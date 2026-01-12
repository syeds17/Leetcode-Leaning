"""
Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach:
- Use two pointers
- One pointer scans the array to find unique elements
- Another pointer keeps track of the position to place the next unique element
- Compare current element with the previous one
- If they are different, place the element at the next position
- Continue until the end of the array

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        for i in range (1,n):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k += 1
        return k     
