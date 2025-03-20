from typing import List


class Solution:

    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        curr1 = [[0] * 2 for _ in range(3)]
        next1 = [[0] * 2 for _ in range(3)]

        # Iterate from the last day to the first
        for i in range(n - 1, -1, -1):
            for k in range(1, 3):

                # Calculate for buy state
                curr1[k][1] = max(-prices[i] + next1[k][0], next1[k][1])

                # Calculate for sell state
                curr1[k][0] = max(prices[i] + next1[k - 1][1], next1[k][0])

            # Move current state to next, for the
            # next iteration
            next1 = [row[:] for row in curr1]

        # The result is the maximum profit starting
        # from day 0, with 2 transactions, and in
        # buy state = 1 (this show that transaction
        # has been completed)
        return curr1[2][1]
