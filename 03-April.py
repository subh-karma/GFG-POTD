class Solution:
    def orangesRotting(self, mat):
        
        q = [(i,j) for i, r in enumerate(mat) for j,e in enumerate(r) if e ==2]
        m,n,t = len(mat), len(mat[0]), 0
        while q:
            nq = []
            for r0, c0, in q:
                for r,c in ((r0+1, c0), (r0-1, c0), (r0, c0+1), (r0, c0-1)):
                    if 0 <= r < m and 0 <= c < n and mat[r][c] == 1:
                        nq.append((r,c))
                        mat[r][c] = 2
            if nq:
                q = nq
                t += 1
            q = nq
        return -1 if any([e == 1 for r in mat for e in r]) else t
