class Solution:
    def kthSmallest(self, mat, k):
        # code here
        new_mat=[]
        for i in mat:
            for j in i:
                new_mat.append(j)
        new_mat.sort()
        return new_mat[k-1]
        # code here
        
