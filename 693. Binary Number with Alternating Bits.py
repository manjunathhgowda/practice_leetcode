class Solution(object):
    def hasAlternatingBits(self, n):
        prev = n & 1
        n >>= 1

        while n:
            curr = n & 1
            if curr == prev:
                return False
            prev = curr
            n >>= 1

        return True

if __name__ == "__main__":
    sol = Solution()

    test_cases = [5, 7, 11, 10, 21]

    for num in test_cases:
        print(f"{num} -> {sol.hasAlternatingBits(num)}")
