class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        arr.sort(reverse=True)
        total = 0
        i = 0
        while i < len(arr) - 1:
            if arr[i] - arr[i+1] < k:
                total += arr[i] + arr[i+1]
                i += 2
            else:
                i += 1
        return total
        # code here
        
