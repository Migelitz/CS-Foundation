class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointers
        k = 0
        l = 1

        while l < len(nums):
            if nums[k] == nums[l]:
                l += 1
            else:
                k += 1
                nums[k] = nums[l]
        return k + 1  

# July 5 2026
# Documentary: I didn't add the edge case of "if len(nums) == 0: return k" since the constraint said 1 <= nums.length <= 3 * 10^4. This code checks if two pointers are same,
# then move l pointer until it found a the unique number and increment pointer k then copy the number in pointer l. After iterating, return k + 1 since we're counting the number of unique
# numbers in an array

# Time complexity: O(n)
# Space Complexity: O(1) 
