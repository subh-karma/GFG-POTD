class Solution:
    def swapDiagonal(self, mat):
        # code here
        n = len(mat[0])
        
        major = []
        minor = []
        
        for i in range(0, n):
            major.append(mat[i][i])
            minor.append(mat[i][n-1-i])
          
        for i in range(0, n):
            mat[i][i] = minor[i]
            mat[i][n-1-i] = major[i]
            
        return mat
      # code here
