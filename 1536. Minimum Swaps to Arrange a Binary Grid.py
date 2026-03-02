from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []

        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        for i in range(n):
            needed = n - 1 - i
            j = i

            while j < n and trailing_zeros[j] < needed:
                j += 1

            if j == n:
                return -1

            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                swaps += 1
                j -= 1

        return swaps


if __name__ == "__main__":
    sol = Solution()

    print(sol.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))   
    print(sol.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))  
    print(sol.minSwaps([[1,0,0],[1,1,0],[1,1,1]]))  