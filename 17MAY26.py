class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        ret=[]
        for ve in arr:
            if ret and ((ret[-1]<0 and ve>=0) or (ret[-1]>=0 and ve<0)):
                ret.pop()
            else:
                ret.append(ve)
        return ret


        # code here
