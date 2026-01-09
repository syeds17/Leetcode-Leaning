"""
Problem: Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Approach:
- Use two pointers (left at start, right at end)
- Compare squares of both ends
- Place the larger square at the end of the result array
- Move pointers accordingly

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        for num in nums:
            sqr.append(num*num)
        sqr.sort()
        return sqr    
