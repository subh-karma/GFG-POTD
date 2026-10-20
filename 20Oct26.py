class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        ret=[]
        l,r=0,1
        cur=arr[l]%2
        for r in range(1,len(arr)):
            if arr[r]%2==cur:
                continue
            ret.extend(sorted(arr[l:r],reverse=True))
            l=r
            cur=arr[r]%2
        return ret+sorted(arr[l:r+1],reverse=True)
        # code here
        
