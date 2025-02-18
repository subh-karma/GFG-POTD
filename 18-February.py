class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for x,y in points:
            temp=x*x+y*y
            temp**=0.5
            res.append([[x,y],temp])
        ans=sorted(res,key=lambda i:i[1])[:k]
        ans=[i[0] for i in ans]
        return ans
