class Solution:
    def minDeletions(self, arr):
        from bisect import bisect_left
        lis = []
        for a in arr:
            i = bisect_left(lis, a)
            if i == len(lis):
                lis.append(a)
            else:
                lis[i] = a
        return len(arr) - len(lis)
        # code here
        
