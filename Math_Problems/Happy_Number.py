"""
Problem: Happy Number
Link: https://leetcode.com/problems/happy-number/

Approach:
- Start with the given number and repeatedly replace it with the sum of the squares of its digits
- Use a set to track numbers seen so far to detect cycles
- If the number becomes 1, it is a happy number; if a cycle is detected, it is not

Time Complexity: O(log n) per iteration, overall depends on cycle length
Space Complexity: O(log n) for storing numbers in the set
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            exp = 0
            for ch in str(n):
                exp += int(ch) ** 2
            n = exp

        return True
            


        
