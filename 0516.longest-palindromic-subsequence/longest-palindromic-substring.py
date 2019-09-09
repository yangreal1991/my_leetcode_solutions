import numpy as np

class Solution:
    """Class of the solution to the question 0516.Longest Palindromic Subsequence

    """
    def __init__(self):
        pass

    def longestPalindromeSubseq(self, s):
        """Given a string s, find the longest palindromic substring in s.

        Idea: A = s, B = s.reverse(). Then check the longest common subsequence
        on A and B.
        f(n, m): longest common subsequence for A[0..n-1] and B[0..m-1]
        f(n, m) = max(f(n-1, m), f(n, m-1)) if A[n] != B[m]
        f(n, m) = 1 + f(n-1, m-1) if A[n] == B[m]

        Time complexity: O(N^2) where N = len(nums)

        Args:
            s: str -- the given string

        Returns:
            result: int -- the longest palindromic substring

        """

        if len(s) == 1:
            return 1

        A = s
        B = s[::-1]

        f = [ [0 for _ in range(len(B)+1) ] for _ in range(len(A)+1) ]

        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
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
        return f[len(A)][len(B)]

class Solution_Recursion:
    """Class of the solution to the question 0516.Longest Palindromic Subsequence

    """
    def __init__(self):
        pass

    def longestPalindromeSubseq(self, s):
        """Given a string s, find the longest palindromic substring in s.

        Idea: A = s, B = s.reverse(). Then check the longest common subsequence
        on A and B.
        f(n, m): longest common subsequence for A[0..n-1] and B[0..m-1]
        f(n, m) = max(f(n-1, m), f(n, m-1)) if A[n] != B[m]
        f(n, m) = 1 + f(n-1, m-1) if A[n] == B[m]

        Time complexity: O(N^2) where N = len(nums)

        Args:
            s: str -- the given string

        Returns:
            result: int -- the longest palindromic substring

        """

        if len(s) == 1:
            return 1

        A = s
        B = s[::-1]

        f = np.ones((len(A) + 1, len(B) + 1), dtype=int) * (-1)
        f[0, :] = 0
        f[:, 0] = 0
        def recur(i, j):
            if f[i, j] == -1:
                if A[i - 1] == B[j - 1]:
                    f[i, j] = 1 + recur(i - 1, j - 1)
                else:
                    f[i, j] = max(recur(i - 1, j), recur(i, j - 1))
            return f[i, j]

        result = recur(len(A), len(B))

        return result

if __name__ == '__main__':
    s = Solution()
    s2 = Solution_Recursion()

    str1 = "babad"
    print(s.longestPalindromeSubseq(str1))
    print(s2.longestPalindromeSubseq(str1))


    str2 = "abbc"
    print(s.longestPalindromeSubseq(str2))
    print(s2.longestPalindromeSubseq(str2))

    str3 = "abdaebdadeabac"
    print(s.longestPalindromeSubseq(str3))
    print(s2.longestPalindromeSubseq(str3))

    str4 = "dddddddddddddddddddddddd"
    print(s.longestPalindromeSubseq(str4))
    print(s2.longestPalindromeSubseq(str4))



