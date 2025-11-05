class Solution:
    def minSquares(self, n):
        from functools import lru_cache
        import bisect
        sqs=[x*x for x in range(1,101)]
        @lru_cache(None)
        def dfs(n=n):
            nonlocal sqs
            if n==0:
                return 0
            mn=float('inf')
            ix=bisect.bisect_right(sqs,n)-1
            for i in range(ix,-1,-1):
                sq=sqs[i]
                mn=min(mn,1+dfs(n-sq))
            return mn
        return dfs()

		# Code here
		
