class Solution:

    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here


        mini=min(s1,s2)
        maxi=max(s1,s2)
        st=1
        e=n*mini
        ans=-1
        while st<=e:
            mid=(st+(e-st)//2)
            sc1=mid//mini
            sc2=mid//maxi
            if sc1+sc2>=n:
                ans=mid
                e=mid-1
            else:
                st=mid+1

        return ans
