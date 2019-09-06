class Solution:
    """Class of the solution to the question 0016.3Sum-closest
    This is a brutal-force solution.
    Time: O( n^3 )

    """
    def threeSumClosest(self, nums, target):
        """Return the summation of 3 numbers that is closest to the target value

        Args:
            nums: List[int] -- the list of the integers
            target: int -- target value

        Returns:
            result: int -- closest summation

        """
        if len(nums) < 2:
            return "Need equal to or more than three numbers!"

        if len(nums) == 2:
            return sum(nums)

        diff_closet = 1e10
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for l in range(j + 1, len(nums)):
                    if diff_closet > abs(nums[i] + nums[j] + nums[l] - target):
                        diff_closet = abs(nums[i] + nums[j] + nums[l] - target)
                        result = nums[i] + nums[j] + nums[l]
        return result

class Solution_Fast:
    """Class of the solution to the question 0015.3Sum
    This is a faster solution.
    Time: O( n^2 * log(N) )

    """

    def search_closest(self, nums, target):
        """Return smallest difference between target and the array of numbers

        Args:
            nums: List[int] -- the list of integers
            target: target value

        Returns:
            result: int -- smallest difference
            nums[mid]: int -- the number in `nums` achieving smallest diff

        """

        if len(nums) == 1:
            return  abs(target - nums[0]), nums[0]

        i = 0
        j = len(nums) - 1
        result = 1e10
        num = 0
        while i <= j:
            mid = int((i + j) / 2)
            if result > abs(target - nums[mid]):
                result = abs(target - nums[mid])
                num = nums[mid]
            if nums[mid] == target:
                return 0, nums[mid]
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return result, num

    def threeSumClosest(self, nums, target):
        """Return the summation of 3 numbers that is closest to the target value

        Args:
            nums: List[int] -- the list of the integers
            target: int -- target value

        Returns:
            result: int -- closest summation

        """

        if len(nums) < 3:
            return "Length of the array must be greater than 2."

        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        diff_closet = 1e10
        for i in range(len(nums) - 2):
            for j in range(i+2, len(nums)):
                c,l = self.search_closest(nums[i+1:j], target - nums[i] - nums[j])
                if c == 0:
                    return nums[i] + nums[j] + l
                else:
                    if diff_closet > c:
                        diff_closet = c
                        result = nums[i] + nums[j] + l
        return result

class Solution_TwoPointer:
    """Class of the solution to the question 0016.3Sum-closest
    This is a two pointer solution.
    Time: O( n^2 )

    """

    def threeSumClosest(self, nums, target):
        """Return the summation of 3 numbers that is closest to the target value

        Args:
            nums: List[int] -- the list of the integers
            target: int -- target value

        Returns:
            result: int -- closest summation

        """


        if len(nums) < 3:
            return "Length of the array must be greater than 2."

        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        max_diff = float("inf")
        result = 0

        for i in range(len(nums)):
            j = i + 1
            l = len(nums) - 1
            while j < l:
                t = nums[i] + nums[j] + nums[l]
                if max_diff > abs(t - target):
                    max_diff = abs(t - target)
                    result = t
                if t > target:
                    l = l - 1
                elif t < target:
                    j = j + 1
                else:
                    return t
        return result

import sys
import random

if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution_Fast()
    s3 = Solution_TwoPointer()
    nums1 = [-4, -1, 1, 2]
    target1 = 1
    print("BF:", s1.threeSumClosest(nums1, target1))
    print("Fast:", s2.threeSumClosest(nums1, target1))
    print("Two_pointers:", s3.threeSumClosest(nums1, target1))


    nums2 = [-2, 1, 2, 3, 4, -1, -4, -2, 5, 2, 3, 0, 1]
    target2 = 10
    print("BF:", s1.threeSumClosest(nums2, target2))
    print("Fast:", s2.threeSumClosest(nums2, target2))
    print("Two_pointers:", s3.threeSumClosest(nums2, target2))

    nums3 = [-1, -1, 0, 0, 0, 1, 2]
    target3 = 5
    print("BF:", s1.threeSumClosest(nums3, target3))
    print("Fast:", s2.threeSumClosest(nums3, target3))
    print("Two_pointers:", s3.threeSumClosest(nums3, target3))

    nums4 = [-9, -9, -6, -6, -4, -4, -4, -3, -3, -1]
    target4 = 0
    print("BF:", s1.threeSumClosest(nums4, target4))
    print("Fast:", s2.threeSumClosest(nums4, target4))
    print("Two_pointers:", s3.threeSumClosest(nums4, target4))

    # Offline Test
    n_tests = 1000
    for _ in range(n_tests):
        nums_test = [random.randint(-10000, 10000) for _ in range(30)]
        target_test = 100
        solution_bf = s1.threeSumClosest(nums_test, target_test)
        solution_fast = s2.threeSumClosest(nums_test, target_test)
        solution_two_pointer = s3.threeSumClosest(nums_test, target_test)
        print("BF:", solution_bf)
        print("Fast:", solution_fast)
        if (abs(solution_bf - target_test) != abs(solution_fast - target_test)) \
            or (abs(solution_bf - target_test) != abs(solution_two_pointer - target_test)) :
            print(nums_test)
            print("An error occurs!")
            sys.exit()
    print("All test passes! Congrats and submit!")


