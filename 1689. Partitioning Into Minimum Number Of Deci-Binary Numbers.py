class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(d) for d in n)


if __name__ == "__main__":
    sol = Solution()

    print(sol.minPartitions("32"))                  
    print(sol.minPartitions("82734"))               
    print(sol.minPartitions("27346209830709182346"))