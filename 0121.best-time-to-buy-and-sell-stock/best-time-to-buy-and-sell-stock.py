class Solution:

    def __init__(self):
        pass

    def maxProfit_BF(self, prices):
        """Say you have an array for which the ith element is the price of a given stock on day i.
        Find the maximum profit under the constraint that only one transaction is permitted.

        Args:
            prices: List[int]

        Returns:
            result: int

        """

        if len(prices) < 2:
            return 0

        result = 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                result = max(result, prices[j] - prices[i])
        return result

    def maxProfit(self, prices):
        """Say you have an array for which the ith element is the price of a given stock on day i.
        Find the maximum profit under the constraint that only one transaction is permitted.

        Args:
            prices: List[int]

        Returns:
            result: int

        """

        if len(prices) < 2:
            return 0

        result = 0
        min_price_before = prices[0]
        for i in range(1, len(prices)):
            result = max(result, prices[i] - min_price_before)
            min_price_before = min(min_price_before, prices[i])

        return result

import random
import sys

if __name__ == '__main__':
    s = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(prices)
    print(s.maxProfit(prices))
    print(s.maxProfit_BF(prices))

    n_runs = 1000
    for i in range(n_runs):
        if i % 100 == 0:
            print("Iteration: ", i)
        prices = [random.randrange(1, 10000, 1) for _ in range(i + 1)]
        if s.maxProfit(prices) != s.maxProfit_BF(prices):
            print(prices)
            print(s.maxProfit(prices))
            print(s.maxProfit_BF(prices))
            sys.exit(0)
    print("All tests passed!!")


