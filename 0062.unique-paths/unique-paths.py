class Solution:

    def __init__(self):
        pass

    def uniquePaths(self, m, n):
        """Return number of possible unique paths

        Args:
            m: int -- number of columns
            n: int -- number of rows

        Returns:
            result: int

        """

        if m == 1 or n == 1:
            return 1

        f = [ [0 for _ in range(m) ] for _ in range(n) ]

        for j in range(m):
            f[0][j] = 1
        for i in range(n):
            f[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        result = f[n - 1][m - 1]
        return result

import random
import sys

if __name__ == '__main__':
    s = Solution()

    m, n = 7, 3
    print(s.uniquePaths(m, n))

    m, n = 1, 2
    print(s.uniquePaths(m, n))

    m, n = 100, 100
    print(s.uniquePaths(m, n))

    m, n = 1000, 1000
    print(s.uniquePaths(m, n))



