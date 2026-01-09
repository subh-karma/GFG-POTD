class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        from collections import Counter
        
        cnt = Counter()
        left = 0
        ans = 0
        
        for r, e in enumerate(arr):
            cnt[e] += 1
            while len(cnt) > k and left <= r:
                cnt[arr[left]] -= 1
                if cnt[arr[left]] == 0:
                    cnt.pop(arr[left])
                left += 1
            ans += r-left+1
        return ans
        # Code here
        
