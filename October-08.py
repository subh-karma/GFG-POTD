from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        maxi=0
        ma=0
        for i in range(len(arr)):
            if arr[i]>maxi :
                ma=maxi
                maxi=arr[i]
            elif arr[i]>ma:
                ma=arr[i]
        return maxi+ma
