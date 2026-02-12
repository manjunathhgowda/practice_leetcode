class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0

        for i in range(n):
            count = {}

            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1

                values = count.values()
                if len(set(values)) == 1:
                    ans = max(ans, j - i + 1)

        return ans
print(Solution().longestBalanced("abbac"))    # 4
print(Solution().longestBalanced("zzabccy"))  # 4
print(Solution().longestBalanced("aba"))      # 2
