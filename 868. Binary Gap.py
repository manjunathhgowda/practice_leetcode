class Solution(object):
    def binaryGap(self, n):
        last = -1
        pos = 0
        ans = 0

        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, pos - last)
                last = pos
            n >>= 1
            pos += 1

        return ans
if __name__ == "__main__":
    sol = Solution()

    print(sol.binaryGap(22))  # 2
    print(sol.binaryGap(8))   # 0
    print(sol.binaryGap(5))   # 2