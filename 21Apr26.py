import math

class Solution:
    def pour(self, fromCap, toCap, d):
        fromJug = fromCap   # fill from jug
        toJug = 0
        step = 1

        while fromJug != d and toJug != d:
            # pour water
            temp = min(fromJug, toCap - toJug)
            toJug += temp
            fromJug -= temp
            step += 1

            # check if done
            if fromJug == d or toJug == d:
                break

            # if from jug empty → refill
            if fromJug == 0:
                fromJug = fromCap
                step += 1

            # if to jug full → empty
            if toJug == toCap:
                toJug = 0
                step += 1

        return step

    def minSteps(self, m, n, d):
        # If impossible
        if d > max(m, n):
            return -1
        
        if d % math.gcd(m, n) != 0:
            return -1
        
        # Try both directions and take minimum
        return min(self.pour(m, n, d), self.pour(n, m, d))
		# Code here
