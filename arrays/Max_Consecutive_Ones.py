"""
Problem: Max Consecutive Ones
Link: https://leetcode.com/problems/max-consecutive-ones/

Approach:
- Iterate through the binary array
- Keep a count of consecutive 1s
- Update the maximum count when 0 is encountered

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        zeros=0
        for num in nums:
            if(num==1):
                zeros += 1
                ans = max(ans,zeros)
            else:
                zeros=0    

        return ans        
