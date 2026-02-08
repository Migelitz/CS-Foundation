class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = 0
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
