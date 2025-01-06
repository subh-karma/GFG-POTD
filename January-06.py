#User function Template for python3
class Solution:
    
    # 25^91/24
    
    def sumClosest(self, arr, target):
        arr.sort()
        ans=[0,float("inf")]
        l,h=0,len(arr)-1
        while l<h:
            val=arr[l]+arr[h]
            if abs(sum(ans)-target)>abs(val-target):
                ans[0],ans[1]=arr[l],arr[h]
            if target<val:
                h-=1
            else:
                l+=1
        return ans if len(arr)!=1 else []







