class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n = len(s)
        freq = {}
        left = 0
        best = -1

        for right in range(n):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            while len(freq) > k:
                lch = s[left]
                freq[lch] -= 1
                if freq[lch] == 0:
                    del freq[lch]
                left += 1

            if len(freq) == k:
                best = max(best, right - left + 1)

        return best
        # code here
        
        
