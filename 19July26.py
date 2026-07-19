class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        next_peak, next_valley = list(range(n)), list(range(n))
        for i in reversed(range(n - 1)):
            if arr[i] == arr[i + 1]:
                next_peak[i] = next_peak[i + 1]
                next_valley[i] = next_valley[i + 1]
            elif arr[i] > arr[i + 1]:
                next_valley[i] = next_valley[i + 1]
            else:
                next_peak[i] = next_peak[i + 1]
        return [(p := next_peak[l]) >= r or next_valley[p] >= r for l, r in queries]
        # code here
        
