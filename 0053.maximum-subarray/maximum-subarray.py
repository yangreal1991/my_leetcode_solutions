class Solution:
    """Class of the solution to the question 0053.Maximum Subarray

    """
    def __init__(self):
        pass

    def maxSubArray(self, nums):
        """Given an integer array nums,
        find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.

        Idea:
        f(n): maximum subarray for nums[0..n-2] and the last number is nums[n-1]
        f(n) = max(nums[n-1], nums[n-1] + f(n-1))

        Time complexity: O(N) where N = len(nums)

        Args:
            nums: List[int] -- the given array of numbers

        Returns:
            result: int -- the largest sum

        """
        if len(nums) < 1:
            return "Error! The length must be greater than 1."

        if len(nums) == 1:
            return nums[0]

        f = []
        f.append(nums[0])
        for i in range(1, len(nums)):
            f.append(max(nums[i], nums[i] + f[i - 1]))

        return max(f)

if __name__ == '__main__':
    s = Solution()

    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums1))

    nums2 = [-2,1,-3,-4,-1,2,1,-5,4]
    print(s.maxSubArray(nums2))


