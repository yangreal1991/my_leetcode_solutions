import numpy as np

class Solution:

    def __init__(self):
        pass

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Given two strings, find the longest common subsequence.

        Idea: Dynamic Programming
        f(n, m): longest common subsequence for A[0..n-1] and B[0..m-1]
        f(n, m) = max(f(n-1, m), f(n, m-1)) if A[n] != B[m]
        f(n, m) = 1 + f(n-1, m-1) if A[n] == B[m]

        Time complexity: O(N^2) where N = len(nums)

        Args:
            text1: str -- one string given
            text2: str -- another string given

        Returns:
            result: int -- the length of the longest common subsequence

        """

        f = [ [0 for _ in range(len(text2)+1) ] for _ in range(len(text1)+1) ]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    f[i + 1][j + 1] = 1 + f[i][j]
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])

        # helper function when we need to reconstruct the subsequence
        # def recon(i, j):
        #     if i == 0 or j == 0:
        #         return []
        #     elif A[i-1] == B[j-1]:
        #         return recon(i-1, j-1) + [A[i-1]]
        #     elif f[i - 1, j] > f[i, j - 1]:
        #         return recon(i - 1, j)
        #     else:
        #         return recon(i, j - 1)

        # result = recon(len(A), len(B))
        return f[len(text1)][len(text2)]

if __name__ == '__main__':
    s = Solution()

    text1 = "abcde"
    text2 = "ace"
    print(s.longestCommonSubsequence(text1, text2))

    text1 = "abc"
    text2 = "def"
    print(s.longestCommonSubsequence(text1, text2))

    text1 = "dddddddddddddddddddddddd"
    text2 = "dddddddddddddddddddddddd"
    print(s.longestCommonSubsequence(text1, text2))



