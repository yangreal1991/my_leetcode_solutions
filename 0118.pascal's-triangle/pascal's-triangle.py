class Solution:

    def __init__(self):
        pass

    def generate(self, numRows):
        """Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

        Args:
            numRows: int

        Returns:
            result: List[List[[int]]

        """
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        result = [[1]]
        a = [1]
        for _ in range(numRows - 1):
            b=[1]
            for j in range(len(a)-1):
                b = b + [a[j] + a[j + 1]]
            b = b + [1]
            result.append(b)
            a = b
        return result

if __name__ == '__main__':
    s = Solution()

    numRows=10
    print(s.generate(numRows))



