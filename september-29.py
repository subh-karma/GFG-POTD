class Solution:
    def totalCount(self, k, arr):
        # code here
        total_segments = 0
        for x in arr:
            # Calculate the number of segments for each element x
            total_segments += (x // k) + (1 if x % k != 0 else 0)
        return total_segments
