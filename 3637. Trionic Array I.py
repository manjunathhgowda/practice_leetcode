class Solution(object):
    def isTrionic(self, nums):
        if len(nums) < 4:
            return False

        res = []
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                if not res or res[-1] != 1:
                    res.append(1)
            elif nums[i] > nums[i + 1]:
                if not res or res[-1] != 0:
                    res.append(0)
            else:
                return False
        
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                return False
        
        return len(res) >= 3

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [1, 3, 5, 4, 2, 6],   # True
        [2, 1, 3],            # False
        [1, 2, 3, 2, 3],      # True
        [1, 2, 3, 2, 1],      # False
        [1, 2, 2, 3],         # False
        [5, 4, 3, 2, 1],      # False
    ]

    for nums in test_cases:
        print(f"nums = {nums} -> {sol.isTrionic(nums)}")
