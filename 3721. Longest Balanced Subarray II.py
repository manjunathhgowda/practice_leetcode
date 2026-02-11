class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1

        self.min_tree = [0] * (2 * self.size)
        self.max_tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)

    def push(self, idx, l, r):
        if self.lazy[idx] != 0:
            self.min_tree[idx] += self.lazy[idx]
            self.max_tree[idx] += self.lazy[idx]

            if l != r:
                self.lazy[2 * idx] += self.lazy[idx]
                self.lazy[2 * idx + 1] += self.lazy[idx]

            self.lazy[idx] = 0

    def update_range(self, l, r, delta, idx, segL, segR):
        self.push(idx, segL, segR)

        if r < segL or l > segR:
            return

        if l <= segL and segR <= r:
            self.lazy[idx] += delta
            self.push(idx, segL, segR)
            return

        mid = (segL + segR) // 2
        self.update_range(l, r, delta, 2 * idx, segL, mid)
        self.update_range(l, r, delta, 2 * idx + 1, mid + 1, segR)

        self.min_tree[idx] = min(
            self.min_tree[2 * idx],
            self.min_tree[2 * idx + 1]
        )
        self.max_tree[idx] = max(
            self.max_tree[2 * idx],
            self.max_tree[2 * idx + 1]
        )

    def query_first_zero(self, l, r, idx, segL, segR):
        self.push(idx, segL, segR)

        if r < segL or l > segR:
            return -1

        if self.min_tree[idx] > 0 or self.max_tree[idx] < 0:
            return -1

        if segL == segR:
            if self.min_tree[idx] == 0:
                return segL
            return -1

        mid = (segL + segR) // 2
        left = self.query_first_zero(l, r, 2 * idx, segL, mid)
        if left != -1:
            return left

        return self.query_first_zero(l, r, 2 * idx + 1, mid + 1, segR)

    def updateRange(self, l, r, delta):
        self.update_range(l, r, delta, 1, 0, self.size - 1)

    def queryFirstZero(self, l, r):
        return self.query_first_zero(l, r, 1, 0, self.size - 1)


class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        segTree = SegmentTree(n)
        lastOccurrence = {}
        maxLen = 0

        for j in range(n):
            v = nums[j]
            old_f = lastOccurrence.get(v, -1)

            L = old_f + 1
            R = j

            # odd → +1, even → -1
            if v % 2 == 1:
                segTree.updateRange(L, R, 1)
            else:
                segTree.updateRange(L, R, -1)

            lastOccurrence[v] = j

            i = segTree.queryFirstZero(0, j)
            if i != -1:
                length = j - i + 1
                maxLen = max(maxLen, length)

        return maxLen


if __name__ == "__main__":
    nums = [36, 39, 35, 1, 52, 10, 17, 20]

    solution = Solution()
    result = solution.longestBalanced(nums)

    print("Input:", nums)
    print("Longest Balanced Length:", result)
