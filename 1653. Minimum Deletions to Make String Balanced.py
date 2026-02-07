class Solution(object):
    def minimumDeletions(self, s):
        deletions = 0
        count_b = 0

        for ch in s:
            if ch == 'b':
                count_b += 1
            else: 
                deletions = min(deletions + 1, count_b)

        return deletions
if __name__ == "__main__":
    sol = Solution()

    print(sol.minimumDeletions("aababbab"))    # 2
    print(sol.minimumDeletions("bbaaaaabb"))   # 2
    print(sol.minimumDeletions("aaaa"))        # 0
    print(sol.minimumDeletions("bbbb"))        # 0
