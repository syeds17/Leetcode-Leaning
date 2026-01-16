"""
Problem: Height Checker
Link: https://leetcode.com/problems/height-checker/

Approach:
- Make a sorted copy of the original heights array
- Compare each element with the original array
- Count the number of positions where the heights differ

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        expected = sorted(heights)
        x = 0
        for i in range(0,n):
            if heights[i] != expected[i]:
                x += 1
        return x        
                
