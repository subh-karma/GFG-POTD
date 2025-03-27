class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        
        n = len(arr)
        i, j = 0,0
        platforms = 0
        max_platforms = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                max_platforms = max(max_platforms, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1
        return max_platforms
        # code here
