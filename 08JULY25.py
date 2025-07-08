from collections import defaultdict
class Solution:
    def findGreater(self, arr):
        #sam
        
        mp = defaultdict(int)
        for i in arr:
            mp[i]+=1
        result = []
        stack = []
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            while stack and stack[-1][1]<=mp[curr]:
                stack.pop()
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1][0])
            stack.append((curr,mp[curr]))
        return result[::-1]
        # code here
        
