class Solution(object):
    """Class of the solution to the question 0011.container-with-most-water
    This is a brutal-force solution.

    """
    def __init__(self):
        pass

    def maxArea(self, height):
        """Calculate the max area

        Args:
            height: List[int] -- List of the heights of bars

        Returns:
            result: int -- the maximal container area

        """
        if len(height) < 2:
            return "Wrong! No container can be built by less than 2 lines."

        result = -1
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                if result < area:
                    result = area
        return result

class Solution_TwoPointers(object):
    """Class of the solution to the question 0011.container-with-most-water
    This is a two-pointer solution.

    """
    def __init__(self):
        pass

    def maxArea(self, height):
        """Calculate the maximum area of the container.

        Args:
            height: List[int] -- List of the heights of bars

        Returns:
            result: int -- the maximal container area

        """
        if len(height) < 2:
            return "Wrong! No container can be built by less than 2 lines."

        result = -1
        i = 0
        j = len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            if result < area:
                result = area
            # If height[i] < height[j] then the best result with the ith line
            # being the left line of the container is the above `area`, and vice versa.
            if height[i] < height[j]:
                i = i + 1
            elif height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
                j = j - 1

        return result

if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution_TwoPointers()

    # Case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print ("Brutal Force:", s1.maxArea(height1))
    print ("Two Pointer:", s2.maxArea(height1))

    # Case 2
    height2 = [28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,561,772,271,178,455,449,426,835,143,845,321,214,867,199,967,881,193,973,386,122,633,810,330,907,906,282,136,986,315,860,849,229,632,473,759,87,922,185]

    print ("Brutal Force:", s1.maxArea(height2))
    print ("Two Pointer:", s2.maxArea(height2))