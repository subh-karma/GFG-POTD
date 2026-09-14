class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        hth=len(mat)
        wth=len(mat[0])
        q=[(0,y,) for y in range(hth)]
        seen=set()
        ret=1
        while q:
            nq=[]
            for x,y in q:
                if (x,y,) in seen:
                    continue
                seen.add((x,y,))
                if mat[y][x]==0 or y-1>=0 and mat[y-1][x]==0 or y+1<hth and mat[y+1][x]==0 or x-1>=0 and mat[y][x-1]==0 or x+1<wth and mat[y][x+1]==0:
                    continue
                if x==wth-1:
                    return ret
                if y-1>=0:
                    nq.append((x,y-1,))
                if y+1<hth:
                    nq.append((x,y+1,))
                if x-1>=0:
                    nq.append((x-1,y,))
                if x+1<wth:
                    nq.append((x+1,y,))
            ret+=1
            q=nq
        return -1
        # code here
        
