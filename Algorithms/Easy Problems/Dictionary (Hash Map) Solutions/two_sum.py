class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = dict()

        for i in range(len(nums)):
            y = target - nums[i]
            if y in complement:
                return [i, complement[y]]
            complement[nums[i]] = i

# Time Complexity: O(n)
# Space Complexity: O(n)
