class Solution:
    def transpose(self, mat):
        # code here
        
        
        #CODE TYPE 1 It only applicable in Square Matrix
        n=len(mat)
        res=[]
        for i in range(n):
            l=[]
            for j in range(n):
                l.append(mat[j][i])
            res.append(l)
        return res
        
        
        #CODE TYPE 2 it is appy on both kind of matrix Square or Rectangle
        res=[[mat[i][j] for i in range(len(mat))]for j in range(len(mat[0]))]
        return res
        # code here
        
