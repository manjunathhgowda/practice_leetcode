def longestPalindrome(s):
    res = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1]:          # palindrome check
                if len(substr) > len(res):
                    res = substr
    return res
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"
