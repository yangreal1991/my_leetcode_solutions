class Solution:
    """Class of the solution to the question 0015.3Sum
    This is a brutal-force solution.

    """
    def threeSum(self, nums):
        """Return the lists of which the summation is zero.

        Args:
            nums: List[int] -- the list of the integers

        Returns:
            result: List[List[int]] -- multiple lists of numbers of which the summation is zero

        """
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for l in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[l] == 0:
                        result.add((nums[i], nums[j], nums[l]))
        result = [ list(a) for a in result  ]
        return result

class Solution_Fast:
    """Class of the solution to the question 0015.3Sum
    This is a faster solution.

    """
    def threeSum(self, nums):
        """Return the lists of which the summation is zero.

        Args:
            nums: List[int] -- the list of the integers

        Returns:
            result: List[List[int]] -- multiple lists of numbers of which the summation is zero

        """
        result = set()
        # Create table to store the number of each integer in the `nums`
        d = {}
        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1

        set1 = list(set(nums))
        for i in range(len(set1) - 1):
            for j in range(i + 1, len(set1)):
                l = -set1[i] - set1[j]
                if l in d:
                    if (d[l] == 1 and l != set1[i] and l != set1[j]) \
                    or (d[l] == 2 and (l != set1[i] or l != set1[j])) \
                    or (d[l] > 2):
                        temp = [set1[i], set1[j], l]
                        temp.sort()
                        result.add(tuple(temp))
        result = [list(a) for a in result]

        if 0 in d:
            if d[0] > 2:
                result.append([0,0,0])
        return result

if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution_Fast()
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(s1.threeSum(nums1))
    print(s2.threeSum(nums1))

    nums2 = [-2, 1, 2, 3, 4, -1, -4, -2, 5, 2, 3, 0, 1]
    print(s1.threeSum(nums2))
    print(s2.threeSum(nums2))

    nums3 = [0, 0, 0, -1, -1, 1, 2]
    print(s1.threeSum(nums3))
    print(s2.threeSum(nums3))

