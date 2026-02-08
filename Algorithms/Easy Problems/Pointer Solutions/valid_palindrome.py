class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub('[^A-Za-z0-9]','',s)
        s = clean.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False   
        return True

# Time Complexity: O(n)
# Space Complexity: O(n) because re.sub and .lower() said to create new string which uses memory
