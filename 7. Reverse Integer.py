class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = int(str(x)[::-1])
        rev = sign * rev

        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev

s = Solution()

print(s.reverse(123))     # 321
print(s.reverse(-123))    # -321
print(s.reverse(120))     # 21
print(s.reverse(1534236469))  # 0
