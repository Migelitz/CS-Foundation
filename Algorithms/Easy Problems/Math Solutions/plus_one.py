class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

# July 5, 2026
# Documentary: If the first digit (ones in place value) is not 9 then just add one. Otherwise, make that digit zero until we  found a number that is not 9. 
# Edge case: If all is 9, then just make all zero and add 1 ad the end

# Time Complexity: O(n) 
# Space Complexity: O(1)
