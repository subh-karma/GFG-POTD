class Solution:
    def findMajority(self, arr):
        store = {}
        n = len(arr)
        size = n/3
        res = []
    
        for num in arr:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
    
            if store[num] > size:
            # print(store[num])
                res.append(num)
    
        res = list(set(res))
        res.sort()
        return res


        # code here
