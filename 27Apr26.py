from collections import Counter
class Solution:
    def smallestSubstring(self, s):
        # code here
        n = len(s)
        zero, one, two = -1, -1, -1
        mini = 1e9
        for i in range(n):
            if s[i]=='0':
                zero = i
            elif s[i]=='1':
                one=i
            else:
                two=i
            if zero!=-1 and one!=-1 and two!=-1:
                mini = min(mini, max(zero, one, two) - min(zero, one, two) + 1)
        if zero==-1 or one==-1 or two==-1:
            return -1
        return mini
        # code here
