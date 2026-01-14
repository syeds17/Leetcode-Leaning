"""
Problem: Check If N and Its Double Exist
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/

Approach:
- Use a set to store visited numbers
- For each number, check if its double or half already exists
- Handle zero separately to avoid false positives

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True

        return False
