class Solution:
    def sumSubstrings(self,s):
        sum = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sum += int(s[i:j+1])
        return sum
