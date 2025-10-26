class Solution:
   def minCost(self, arr):
        from heapq import heapify, heappop, heapreplace
        heapify(arr)
        cost = 0
        for _ in range(len(arr) - 1):
            c = heappop(arr) + arr[0]
            cost += c
            heapreplace(arr, c)
        return cost
    # code here
