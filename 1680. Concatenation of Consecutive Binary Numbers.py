class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        length = 0

        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                length += 1
            result = ((result << length) | i) % MOD

        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.concatenatedBinary(1))
    print(sol.concatenatedBinary(3))
    print(sol.concatenatedBinary(12))