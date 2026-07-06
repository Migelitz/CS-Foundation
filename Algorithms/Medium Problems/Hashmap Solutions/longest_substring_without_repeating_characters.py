class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        left = right = max_length = 0

        while right < len(s):
            if s[right] not in seen:
                seen[s[right]] = 0
                right += 1
                max_length = max(max_length, right - left)
            elif s[right] in seen:
                del seen[s[left]]
                left += 1

        return max_length

# July 6, 2026
# Documentary: Uses sliding window and hash map for efficient time complexity in exchange for memory
# Time complexity: O(n)
# Space complexity: O(n)
