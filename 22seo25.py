class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        
        pse = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
            
            
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
            
        res = [0] * (n+1)
        for i in range(n):
            length = nse[i] - pse[i] - 1
            res[length] = max(res[length], arr[i])
            
        for i in range(n-1, 0, -1):
            res[i] = max(res[i], res[i+1])
        
        return res[1:]
       # code here
