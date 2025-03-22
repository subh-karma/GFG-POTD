class Solution:
    def rob_linear(self, nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr
    def maxValue(self, arr):
        if len(arr) == 1:
            return arr[0]
        return max(self.rob_linear(arr[:-1]), self.rob_linear(arr[1:]))
 

