class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        LCP = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return LCP
            LCP += strs[0][i]
        return LCP

# N = Number of strings 
# S = max length of string

# Time Complexity: O(N * S log S) 
# Space Complexity: O(N + S) Tim sort uses temporary space
