import numpy as np

class Solution:

    def __init__(self):
        pass

    def searchInsert(self, nums, target):
        """Given a sorted array and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        Args:
            nums: List[int] -- a sorted array
            target: int -- target value

        Returns:
            result: int -- the the index where it would be if it were inserted in order

        """

        if len(nums) == 0:
            return "Length of nums must be greater than 0."

        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()

    nums = [1,3,5,6]
    target = 5
    print(s.searchInsert(nums, target))



