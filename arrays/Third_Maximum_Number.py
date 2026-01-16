"""
Problem: Third Maximum Number
Link: https://leetcode.com/problems/third-maximum-number/

Approach:
- Keep track of the top three maximum numbers
- Iterate through the array and update the top three
- Return the third maximum if it exists, otherwise return the maximum

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniq = list(set(nums))
        if len(uniq)<3:
            return max(uniq)
        uniq.sort(reverse=True)
        return uniq[2]
        
                
