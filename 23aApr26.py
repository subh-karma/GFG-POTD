class Solution:
    def canSplit(self, arr):
        from bisect import bisect_left
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
        if arr[-1] & 1:  # odd
            return False
        half = arr[-1] // 2
        i = bisect_left(arr, half)
        return arr[i] == half
        #code here
