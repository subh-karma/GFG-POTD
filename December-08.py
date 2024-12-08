class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort(key=lambda x:x[0])
        prev=arr[0]
        result=[]
        for i in range(1,len(arr)):
            if arr[i][0]<=prev[1]:
                prev[1]=max(arr[i][1],prev[1])
            else:
                result.append(prev)
                prev=arr[i]
        result.append(prev)
        return result
