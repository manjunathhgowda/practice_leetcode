from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        base = nums[0]
        need = k - 2

        if need == 0:
            return base + min(nums[1:dist+2])

        left_set = SortedList()
        right_set = SortedList()
        current_sum = 0

        def move_left_to_right():
            nonlocal current_sum
            val = left_set.pop()
            current_sum -= val
            right_set.add(val)

        def move_right_to_left():
            nonlocal current_sum
            val = right_set.pop(0)
            left_set.add(val)
            current_sum += val

        for j in range(2, min(n, 2 + dist)):
            left_set.add(nums[j])

        while len(left_set) > need:
            move_left_to_right()

        current_sum = sum(left_set)
        res = float('inf')

        for i in range(1, n - 1):
            if len(left_set) == need:
                res = min(res, base + nums[i] + current_sum)

            out_idx = i + 1
            in_idx = i + dist + 1

            if out_idx < n:
                val = nums[out_idx]
                if val in left_set:
                    left_set.remove(val)
                    current_sum -= val
                else:
                    right_set.remove(val)

            if in_idx < n:
                val = nums[in_idx]
                if left_set and val < left_set[-1]:
                    left_set.add(val)
                    current_sum += val
                else:
                    right_set.add(val)

            while len(left_set) < need and right_set:
                move_right_to_left()

            while len(left_set) > need:
                move_left_to_right()

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.minimumCost([1,3,2,6,4,2], 3, 3))      
    print(sol.minimumCost([10,1,2,2,2,1], 4, 3))     
    print(sol.minimumCost([10,8,18,9], 3, 1))        