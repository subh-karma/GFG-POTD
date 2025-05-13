class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        
        r = min(r, n - r)
        m = 1

        for i in range(r):
            m = m * (n - i)
            m = m // (i + 1)

        return m
