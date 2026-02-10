class Solution(object):
    def longestBalancedSubarray(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            evens = set()
            odds = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)

        return ans


# -------------------------
# Run Test Cases (VS Code)
# -------------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        [2, 5, 4, 3],
        [3, 2, 2, 5, 4],
        [1, 2, 3, 2],
        [2, 2, 2],
        [1, 3, 5]
    ]

    for nums in tests:
        print(nums, "->", sol.longestBalancedSubarray(nums))
