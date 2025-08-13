class Solution:
    def minSoldiers(self, arr, k):
        # code here
        rem = [] 
        cnt=0
        n = -(-len(arr)//2)
        
        for i in arr:
            if i%k ==0:
                cnt+=1
            else:
                rem.append(k-(i%k))
        if cnt>=n:
            return 0
        rem.sort()
        res=0
        for j in rem:
            res += j
            cnt+=1
            if cnt>=n:
                return res
        return -1


        # code here
        
