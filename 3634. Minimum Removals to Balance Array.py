class Solution(object):
    def minimumRemovals(self, nums, k):
        nums.sort()
        n = len(nums)

        left = 0
        max_len = 1

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([2, 1, 5], 2),
        ([1, 6, 2, 9], 3),
        ([4, 6], 2),
        ([1], 5),
        ([1, 2, 4, 8, 16], 2)
    ]

    for nums, k in test_cases:
        print(f"nums = {nums}, k = {k} -> minimum removals = {sol.minimumRemovals(nums, k)}")
