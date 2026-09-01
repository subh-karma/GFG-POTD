class Solution:
    def palindromicStrings(self, n, k):
        import math
        MODULO = 10 ** 9 + 7
        s = 0
        for i in range(1, n // 2 + 1):
            s = (s + 2 * math.perm(k, i)) % MODULO
        if n & 1:
            s = (s + math.perm(k, (n + 1) // 2)) % MODULO
        return s
            # code here
        
