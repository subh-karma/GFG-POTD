class Solution:
    def longestSubarray(self, arr, x):
        
        from collections import deque
        dqMin = deque()
        dqMax = deque()
        
        resStart, resEnd = 0, 0
        start, end = 0, 0
        
        for idx, num in enumerate(arr):
            
            while dqMin and arr[dqMin[-1]] >= num:
                dqMin.pop()
            dqMin.append(idx)
            
            while dqMax and arr[dqMax[-1]] <= num:
                dqMax.pop()
            dqMax.append(idx)
            
            end = idx
            
            while start < end and ( arr[dqMax[0]] - arr[dqMin[0]] ) > x:
                if start == dqMin[0]:
                    dqMin.popleft()
                if start == dqMax[0]:
                    dqMax.popleft()
                start += 1
            
            #print(start, end, dqMin, dqMax)
            
            if (end - start) > (resEnd - resStart):
                resStart, resEnd = start, end
        
        return arr[resStart : (resEnd + 1)]
                
