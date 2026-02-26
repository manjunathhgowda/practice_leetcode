class Solution(object):
    def numSteps(self, s):
        steps = 0
        num = int(s, 2)

        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            steps += 1

        return steps


if __name__ == "__main__":
    sol = Solution()

    s1 = "1101"
    s2 = "10"
    s3 = "1"

    print(sol.numSteps(s1))
    print(sol.numSteps(s2))
    print(sol.numSteps(s3))