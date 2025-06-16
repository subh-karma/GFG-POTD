class Solution:
    def minCost(self, heights, cost):
        def calc(target):
            return sum(abs(h - target) * c for h, c in zip(heights, cost))
        
        low, high = min(heights), max(heights)
        while low < high:
            mid = (low + high) // 2
            cost_mid = calc(mid)
            cost_next = calc(mid + 1)
            if cost_mid <= cost_next:
                high = mid
            else:
                low = mid + 1
        return calc(low)
        # code here
