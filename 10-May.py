class Solution:
    def longestSubarray(self, a, k):
        m, s, r = {}, 0, 0
        for i in range(len(a)):
            s += 1 if a[i] > k else -1
            if s > 0:
                r = i + 1
            elif s - 1 in m:
                r = max(r, i - m[s - 1])
            if s not in m:
                m[s] = i
        return r
