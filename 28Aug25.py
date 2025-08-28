class Solution:
    def maxOnes(self, arr, k):
        mx=0
        left=0
        kk=k
        for right,ve in enumerate(arr):
            if ve==1:
                mx=max(mx,right-left+1)
                continue
            while left<=right and kk<=0:
                if arr[left]==0:
                    kk+=1
                left+=1
            if kk>0:
                mx=max(mx,right-left+1)
                kk-=1
        return mx
