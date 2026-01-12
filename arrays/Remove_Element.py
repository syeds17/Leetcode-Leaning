"""
Problem: Remove Element
Link: https://leetcode.com/problems/remove-element/

Approach:
- Use two pointers
- One pointer scans the array
- Another pointer keeps track of the position to place elements not equal to the given value
- Compare each element with the given value
- If the element is not equal to the value, place it at the next position
- Continue until the end of the array

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i], nums[n-1] = nums[n-1], nums[i]
                n -= 1
            else:
                i += 1

        return n
