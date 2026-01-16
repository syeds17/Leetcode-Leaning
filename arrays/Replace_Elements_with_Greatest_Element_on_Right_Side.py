"""
Problem: Replace Elements with Greatest Element on Right Side
Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Approach:
- Traverse the array from **right to left**
- Keep track of the **maximum element seen so far**
- Replace the current element with the maximum of the elements to its right
- The last element is replaced with -1

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        x = -1
        for i in range(n-1,-1,-1):
            curr = arr[i]
            arr[i] = x
            x = max(x,curr)
        return arr    
