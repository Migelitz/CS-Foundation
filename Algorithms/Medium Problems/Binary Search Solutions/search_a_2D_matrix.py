class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            low = 0
            high = len(matrix[row]) - 1

            while low <= high:
                mid = (low + high) // 2
                
                if target < matrix[row][mid]:
                    high = mid - 1
                elif target > matrix[row][mid]:
                    low = mid + 1
                elif target == matrix[row][mid]:
                    return True
        return False
                    
# Time Complexity: O(m * log n) - not the most efficient time complexity. Need to find way to achieve O(log n * m)
# Space Complexity: O(1)