class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
if __name__ == "__main__":

    sol = Solution()

    # Example 1
    nums = [2, 7, 11, 15]
    target = 9
    print("Example 1 Output:", sol.twoSum(nums, target))  # [0, 1]

    # Example 2
    nums = [3, 2, 4]
    target = 6
    print("Example 2 Output:", sol.twoSum(nums, target))  # [1, 2]

    # Example 3
    nums = [3, 3]
    target = 6
    print("Example 3 Output:", sol.twoSum(nums, target))  # [0, 1]
