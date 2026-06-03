class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            temp_arr = []

            for j in range(i+1):
                if j == 0:
                    temp_arr.append(1)

                if 0 < j and j < i:
                    temp_arr.append(result[i-1][j] + result[i-1][j-1])

                if 0 < j and i == j:
                    temp_arr.append(1)
            result.append(temp_arr)
        return result

  # Time complexity: O(n^2)
  # Space complexity: O(n^2) - Total space
  # Auxiliary space: O(n)
