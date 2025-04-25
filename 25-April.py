class Solution:
    def majorityElement(self, arr):
        #code here
        hashmap={}
        A = arr
        N = len(arr)
        for i in A:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
            
        for key, val in hashmap.items():
            if val>N/2:
                return key
                
        return -1
