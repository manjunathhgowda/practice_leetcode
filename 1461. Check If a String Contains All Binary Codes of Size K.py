class Solution(object):
    def hasAllCodes(self, s, k):
        # If total possible codes > total substrings, impossible
        if len(s) < k:
            return False

        needed = 1 << k   # 2^k
        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == needed:
                return True

        return False

if __name__ == "__main__":
    sol = Solution()

    print(sol.hasAllCodes("00110110", 2))  # True
    print(sol.hasAllCodes("0110", 1))      # True
    print(sol.hasAllCodes("0110", 2))      # False