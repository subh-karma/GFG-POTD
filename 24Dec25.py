class Solution:
    def countLessEqual(self, arr, x):
        import bisect
        arr.sort()
        return bisect.bisect_right(arr, x)
        #code here
        
