"""
Problem: Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/

Approach:
- Calculate the total sum of the array
- Maintain a running left sum while iterating
- For each index, check if left sum equals (total sum - left sum - current element)
- Return the leftmost index that satisfies the condition

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
         total_sum = sum(nums)
         left_sum = 0

         for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

         return -1
