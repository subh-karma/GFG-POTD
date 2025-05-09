class Solution:
    def findMaximumNum(self, s, k):
        s = list(s)
        n = len(s)
        for i in range(n):
            j = max([(s[j], j) for j in range(i, n)])[1]
            if s[i] != s[j]:
                s[i], s[j] = s[j], s[i]
                k -= 1
            if k == 0:
                break
        return ''.join(s)
