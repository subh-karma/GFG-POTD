class Solution:
    def findPeakGrid(self, mat):
        mx=max(max(rw) for rw in mat)
        for y,rw in enumerate(mat):
            try:
                x=rw.index(mx)
                return (y,x,)
            except:
                continue
        # code here
        
