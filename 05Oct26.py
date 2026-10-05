class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr)+1
        final = []

        for i in range(2,n+1):
            curr = i
            d = 0
            while curr !=1:
                curr = arr[curr-2]
                d+=1
                final.append([i,curr,d])
        final.sort()
        return final
        
