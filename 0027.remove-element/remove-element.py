class Solution:
    """Class of the solution to the question 0027.remove-element

    """
    def __init__(self):
        pass

    def removeElement(self, nums, val):
        """Given an array nums and a value val, we
        remove all instances of that value in-place and return the new length.

        Args:
            nums: List[int] -- the given array of numbers
            val: int -- the value of instances

        Returns:
            result: int -- the length of array after removing the instances of `val`

        """
        if len(nums) == 0:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i = i + 1
        return len(nums), nums

if __name__ == '__main__':
    s = Solution()
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print(s.removeElement(nums1, val1))

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(s.removeElement(nums2, val2))

    nums3 = [1]
    val3 = 1
    print(s.removeElement(nums3, val3))


