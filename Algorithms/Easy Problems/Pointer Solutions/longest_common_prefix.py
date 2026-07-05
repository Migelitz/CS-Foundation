class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or strs[0][i] != j[i]:
                    return result
            result += strs[0][i]

        return result

# February 2026
# Time Complexity: O(N * S log S) 
# Space Complexity: O(N + S) Tim sort uses temporary space

# July 5 2026
# Time and complexity update
# Documentary: Removed the sort() for cheaper time and space. Instead, rely on checking each strings character to first first character iteratively 

# Time Complexity: O(n * m)
# Space Complexity: O(1)
