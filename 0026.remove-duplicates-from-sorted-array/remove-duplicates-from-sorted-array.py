class Solution(object):
    """Class of the solution to the question 0026.remove-duplicates-from-sorted-array

    """
    def __init__(self):
        pass

    def removeDuplicates(self, nums):
        """Return the new length of the array after removing duplicates

        Args:
            nums: List[int] -- the array with duplicate elements

        Return:
            result: int -- the new length of the array

        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    nums0 = [1, 1, 1]
    nums1 = [1, 1, 1, 2, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print (s.removeDuplicates(nums0))
    print (s.removeDuplicates(nums1))
    print (s.removeDuplicates(nums2))

