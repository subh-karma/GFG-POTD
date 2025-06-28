class Solution:
    def countLessEq(self, a, b):
        def binary(arr,target):
            l=0
            r=len(arr)-1
            while l<=r:
                mid=l+(r-l)//2
                if arr[mid]<=target and mid+1<len(arr) and arr[mid+1]>target:
                    return mid
                elif arr[mid]>target:
                    r=mid-1
                elif arr[mid]<=target and mid+1>=len(arr):
                    return mid
                else:
                    l=mid+1
            return -1
        ans=[]
        b.sort()
        for i in a:
            ans.append(binary(b,i)+1)
        return ans

        # code here
        
