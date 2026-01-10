"""
Problem: Duplicate Zeros
Link: https://leetcode.com/problems/duplicate-zeros/

Approach:
- Count the number of zeros in the array
- Use two pointers starting from the end:
  - One pointer for the original array
  - One pointer for the virtual expanded array
- Traverse from right to left to avoid overwriting elements
- When a zero is found, duplicate it by writing twice (if within bounds)

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zer = arr.count(0)
        n = len(arr)
        i = n-1
        j = n+zer-1
        while i<j:
            if (j<n):
                arr[j] = arr[i]
                
            if (arr[i]==0):
                j -=1
                if(j<n):
                    arr[j]=0
            i -= 1
            j -= 1
                
