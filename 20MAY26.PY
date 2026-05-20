class Solution:
    def isProduct(self, arr, target):
        # code here
        n = len(arr)
        mp = {}
        for i in range(n):
            num = arr[i]
            if num == 0:
                if target == 0:
                    return True
                continue
            #a * b = target
            #a = target / b
            if target / num in mp:
                return True
            mp[num] = i
        return False
        # code here
