"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach:
- Create an empty dictionary `seen` to store numbers and their indexes
- Loop through the array with index `i` and value `num` using enumerate
- Calculate `complement = target - num`
- If `complement` exists in `seen`, return `[seen[complement], i]`
- Otherwise, store `num` in `seen` with its index for future reference

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dir = {}
        for i,num in enumerate(nums):
            otherNum = target - num
            if otherNum in dir:
                return [dir[otherNum],i]
            dir[num] = i  
