class Solution(object):
    def countBinarySubstrings(self, s):
        prev = 0
        curr = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1

        ans += min(prev, curr)
        return ans


# -------------------------
# Run Test Cases (VS Code)
# -------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.countBinarySubstrings("00110011"))  # 6
    print(sol.countBinarySubstrings("10101"))     # 4
