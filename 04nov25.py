class Solution:
    def minCost(self, height):
        n = len(height)
        if n == 1:
            return 0
        cost_2, cost_1 = 0, abs(height[1] - height[0])
        for i in range(2, n):
            cost_0 = min(
                cost_1 + abs(height[i] - height[i - 1]),
                cost_2 + abs(height[i] - height[i - 2])
            )
            cost_2 = cost_1
            cost_1 = cost_0
        return cost_1
 

