class Solution:
    def balanceSums(self, mat):
    
        n = len(mat)
        m = len(mat[0])
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(n)) for j in range(m)]
        target = max(max(row_sum), max(col_sum))
    
        total_increments = 0
        i, j = 0, 0
        
        while i < n and j < m:
            diff = min(target - row_sum[i], target - col_sum[j])
            mat[i][j] += diff
            row_sum[i] += diff
            col_sum[j] += diff
            total_increments += diff
            if row_sum[i] == target:
                i += 1
            if col_sum[j] == target:
                j += 1
    
        return total_increments
        # code here
