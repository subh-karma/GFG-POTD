class Solution:
     def countWays(self, n: int, sumi: int) -> int:
        from functools import cache
        if n * 9 < sumi:
            return -1
        
        @cache
        def dfs(i: int, sumi: int) -> int:
            if i == n:
                return int(sumi == 0)
            return sum(dfs(i + 1, sumi - d) for d in range(min(9, sumi) + 1))

        return sum(dfs(1, sumi - d) for d in range(1, 10))
        # code here
        
