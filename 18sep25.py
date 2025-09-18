class Solution:
    def nextGreater(self, arr):
        lth=len(arr)
        ret=[-1]*lth
        stk=[]
        for ix in range(2*lth):
            ix%=lth
            while stk and arr[stk[-1]]<arr[ix]:
                prv=stk.pop()
                ret[prv]=arr[ix]
            stk.append(ix)
        return ret
        # code here
