class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        dp = [[0.0] * 101 for _ in range(101)]
        dp[0][0] = float(poured)

        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    overflow = (dp[i][j] - 1) / 2.0
                    dp[i + 1][j] += overflow
                    dp[i + 1][j + 1] += overflow
                    dp[i][j] = 1.0

        return min(1.0, dp[query_row][query_glass])


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (1, 1, 1),
        (2, 1, 1),
        (4, 2, 1),
        (100000009, 33, 17)
    ]

    for poured, row, glass in test_cases:
        result = sol.champagneTower(poured, row, glass)
        print(f"poured={poured}, row={row}, glass={glass} -> {result:.5f}")
