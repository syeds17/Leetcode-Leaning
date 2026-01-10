"""
Problem: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/

Approach:
- Use three pointers starting from the end of the arrays
- One pointer at the last valid element of nums1
- One pointer at the last element of nums2
- One pointer at the last position of nums1 (including extra space)
- Compare elements from nums1 and nums2 and place the larger one at the end
- Continue until all elements of nums2 are merged

Time Complexity: O(m + n)
Space Complexity: O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i -= 1
                
            else:
                nums1[k]=nums2[j]
                j -= 1
            k -= 1   
