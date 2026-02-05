class Solution(object):
    def transformArray(self, nums):
        n = len(nums)
        result = [0] * n

        for i in range(n):
            new_index = (i + nums[i]) % n
            result[i] = nums[new_index]

        return result
s = Solution()

print(s.transformArray([3, -2, 1, 1]))   # [1, 1, 1, 3]
print(s.transformArray([-1, 4, -1]))     # [-1, -1, 4]
