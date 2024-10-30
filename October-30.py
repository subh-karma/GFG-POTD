class Solution:
    def countPairsWithDiffK(self, arr, k):
        num_set = set(arr)
        count = 0

        for x in num_set:
            if (x + k) in num_set:
                count += arr.count(x) * arr.count(x + k)
                
        return count
