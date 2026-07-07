# No looping
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & n - 1 == 0

# July 7, 2026
# Documentary: If you look at the pattern where the power of 2 (n) and by subtracting 1 (n - 1) gives us 0 common bits. Otherwise its not power of two
# Time complexity: O(1)
# Space complexity: O(1)

# Uses looping
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1

        return True if count == 1 else False

# July 7, 2026
# Documentary: We count the number of turn on bits (1), if we got more than 1 bits, its not power. Since power of two always have 1 bit on (1 = 1, 2 = 10, 4 = 100, 8 = 1000), we could conclude this is safe to do
# Time complexity: O(n)
# Space complexity: O(1)
