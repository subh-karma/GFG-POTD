class Solution:
    def lis(self, arr):
        # code here
        n = len(arr)
        lis = [1] * n
        for i in range(1, n):
            for prev in range(0, i):
                if arr[i] > arr[prev]:
                    lis[i] = max(lis[i], lis[prev] + 1)
    
        return max(lis)

