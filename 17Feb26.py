class Solution:
    def overlapInt(self, arr):
        from collections import defaultdict
        cnt=defaultdict(int)
        for sta,sto in arr:
            cnt[sta]+=1
            cnt[sto+1]-=1
        mx=cur=0
        for ix in sorted(cnt):
            cur+=cnt[ix]
            mx=max(mx,cur)
        return mx
        # code here
        
