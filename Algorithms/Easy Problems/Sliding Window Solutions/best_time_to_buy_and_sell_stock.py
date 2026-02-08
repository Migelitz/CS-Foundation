class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = profit = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            if profit < prices[right] - prices[left]:
                profit = prices[right] - prices[left]
            
        if profit <= 0:
            return 0
        return profit

# Time Complexity: O(n)
# Space Complexity: O(1)
