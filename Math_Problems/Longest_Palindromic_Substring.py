"""
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/

Approach:
- Use expand-around-center technique
- Consider each index as a possible center (single and double center)
- Expand left and right while characters match
- Track the longest palindrome found

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s:
            return ""

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)

            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
