class Solution:
    def convert(self, s, numRows):
        if numRows <= 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        index = 0       # current row
        direction = 1   # 1 = moving down, -1 = moving up

        for ch in s:
            rows[index] += ch

            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1

            index += direction

        return "".join(rows)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print("Input:", s1, "Rows:", numRows1)
    print("Output:", solution.convert(s1, numRows1))
    print()

    # Example 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print("Input:", s2, "Rows:", numRows2)
    print("Output:", solution.convert(s2, numRows2))
    print()

    # Example 3
    s3 = "A"
    numRows3 = 1
    print("Input:", s3, "Rows:", numRows3)
    print("Output:", solution.convert(s3, numRows3))
