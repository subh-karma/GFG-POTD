class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        prev = arr[0]
        for i in range(n - 1):
            arr[i], prev = prev ^ arr[i + 1], arr[i]
        arr[-1] ^= prev
        return arr
        # code here
        
