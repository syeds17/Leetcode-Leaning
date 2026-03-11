"""
Problem: Plus One
Link: https://leetcode.com/problems/plus-one/

Approach:
- Traverse the digits array from the end
- Add one to the last digit
- If the digit becomes 10, set it to 0 and carry over to the next digit
- If all digits become 0, insert 1 at the beginning

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range (n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
                
                
                
