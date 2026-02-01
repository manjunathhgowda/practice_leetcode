def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

test_cases = [
    "abcabcbb",  # Example 1
    "bbbbb",     # Example 2
    "pwwkew"     # Example 3
]

for i, s in enumerate(test_cases, start=1):
    result = lengthOfLongestSubstring(s)
    print(f"Example {i}:")
    print(f"Input: s = \"{s}\"")
    print(f"Output: {result}")
    print("-" * 30)
