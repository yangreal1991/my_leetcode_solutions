import numpy as np

class Solution:

    def __init__(self):
        pass

    def plusOne(self, digits):
        """Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

        Args:
            digits: List[int] -- a non-empty array

        Returns:
            result: List[int] -- a list storing the integer after adding one

        """

        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
        return [1] + digits

if __name__ == '__main__':
    s = Solution()

    digits = [9,9,9]
    print(s.plusOne(digits))

    digits = [1,2,9]
    print(s.plusOne(digits))



