class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        minrange=-2**31
        maxrange=2**31-1
        n=len(s)
        sign=1
        num=0

        i=0

        while i<n and s[i]==' ':
            i+=1

        if i<n and (s[i]=='+' or s[i]=='-'):
            if s[i]=='-':
                sign=-1
            i+=1
        while i<n and s[i].isdigit():
            num=num*10+(ord(s[i])-ord('0'))
        
            if sign*num<=minrange:
                return minrange
            if sign*num>=maxrange:
                return maxrange
            i+=1
        return sign*num

s = Solution()

print(s.myAtoi("42"))          # 42
print(s.myAtoi("   -042"))     # -42
print(s.myAtoi("1337c0d3"))    # 1337
print(s.myAtoi("0-1"))         # 0
print(s.myAtoi("words and 987"))  # 0
