class Solution:
    def uniquePerms(self, arr):
        # code here 
        n = len(arr)
        def permute(sofar, left):
            if len(sofar) == n:
                yield sofar
            else:
                p = None
                for i, e in enumerate(left):
                    if e != p:
                        yield from permute(sofar + [e], left[:i]+left[i+1:])
                    p = e 
        
        return list(permute([], sorted(arr)))
        # code here 
