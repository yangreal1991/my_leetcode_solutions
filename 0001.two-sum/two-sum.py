class Solution(object):
    """Class of the solution to the question 0001.two-sum
    This is a brutal-force solution.

    """
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """Given an array of integers,
        return indices of the two numbers such that they add up to a specific target.

        Args:
            nums: List[int] -- the given array of integers
            target: int -- the specific target one would like to add up to

        Returns:
            result: List[int] -- the indices of the two numbers

        """

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    # since the question statment ensures unique solution, no more action is needed.
                    return result
        return "No Solution."

class Solution_Hash(object):
    """Class of the solution to the question 0001.two-sum
    This is a Hash-Table solution faster than brutal-force.

    """
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """Given an array of integers,
        return indices of the two numbers such that they add up to a specific target.

        Args:
            nums: List[int] -- the given array of integers
            target: int -- the specific target one would like to add up to

        Returns:
            result: List[int] -- the indices of the two numbers

        """

        # create hash table for nums
        hash_table = {}
        for i, num in enumerate(nums):
            hash_table[num] = i

        # one pass and find the index of the residual
        for i, num in enumerate(nums):
            if (target - num in hash_table) and (hash_table[target - num] != i):
                result = [i, hash_table[target - num]]
                return result
        return "No Solution."

if __name__ == '__main__':
    # Case 1
    nums = [2, 7, 13, 22]
    target = 20
    print("Brutal_Force:", Solution().twoSum(nums, target))
    print("Hash:", Solution_Hash().twoSum(nums, target))

    # Case 2
    nums = [3, 2, 4]
    target = 6
    print("Brutal_Force:", Solution().twoSum(nums, target))
    print("Hash:", Solution_Hash().twoSum(nums, target))
