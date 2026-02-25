class Solution(object):
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


if __name__ == "__main__":
    arr1 = [0,1,2,3,4,5,6,7,8]
    arr2 = [1024,512,256,128,64,32,16,8,4,2,1]

    sol = Solution()
    print(sol.sortByBits(arr1))
    print(sol.sortByBits(arr2))