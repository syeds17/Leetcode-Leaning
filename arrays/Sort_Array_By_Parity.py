"""
Problem: Sort Array By Parity
Link: https://leetcode.com/problems/sort-array-by-parity/

Approach:
- Use two pointers: one for iterating through the array, one for placing even numbers at the front
- Traverse the array once
- Swap even numbers with the element at the 'even position' pointer
- Maintain relative order of even and odd numbers is not required

Time Complexity: O(n)
Space Complexity: O(1)  # in-place modification
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        if n==0:
            return nums
        for i in range(0,n):
            if nums[i]%2==0:
                nums[j],nums[i]=nums[i],nums[j]
                j += 1
        return nums        
        
