class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        from collections import defaultdict
        st=defaultdict(set)
        for ix,arr in enumerate([s1,s2,s3]):
            sm=sum(arr)
            st[ix].add(sm)
            tot=0
            for ve in arr:
                tot+=ve
                st[ix].add(sm-tot)
        com=st[0]&st[1]&st[2]
        return max(com) if com else 0
        # code here
        
