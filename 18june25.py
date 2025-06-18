class Solution:
    def palinParts (self, s):
        lth=len(s)
        cur=[]
        ret=[]
        def dfs(ix=0):
            nonlocal s,lth,cur,ret
            if ix>=lth:
                for c in cur:
                    if c!=c[::-1]:
                        return
                ret.append(cur[::])
                return
            cur.append(s[ix])
            dfs(ix+1)
            cur.pop()
            if cur:
                cur[-1]+=s[ix]
                dfs(ix+1)
                cur[-1]=cur[-1][:-1]
        dfs()
        return ret
