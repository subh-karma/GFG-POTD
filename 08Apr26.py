class Solution:
    def segregate0and1(self, arr):
        # code here
        n = len(arr)
        zero = 0
        while zero<n and arr[zero]==0:
            zero+=1
        if zero==n:
            return 
        for i in range(zero,n):
            if arr[i]==0:
                arr[i],arr[zero] = arr[zero],arr[i]
                zero+=1
      # code here02
