class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low = 1
        high = x // 2 # The square root of x (where x >= 2) is never greater than x/2

        while low <= high:
            mid = low + (high - low) // 2

            # Using mid <= x // mid to avoid overflow and ZeroDivision
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                high = mid - 1
            else:
                low = mid + 1
        
        # When the loop ends, 'high' is the floor of the square root
        return high
    
# Time Complexity: O(log n)
# Time Complexity: O(1)