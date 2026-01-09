"""
Problem: Find Numbers with Even Number of Digits
Link: https://leetcode.com/explore/
Approach:
- Convert each number to string
- Count digits using len()
- Check if digit count is even

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            digits = len(str(num))

            if digits % 2 == 0:
                count += 1

        return count
        
