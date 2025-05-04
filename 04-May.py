from collections import defaultdict

class Solution:
    def findSubString(self, str):
        n=len(set(str))
        
        left, freq,output=0,defaultdict(int), float('inf')
        for i in range(len(str)):
            freq[str[i]]+=1
            while left<=i and len(freq)==n:
                output=min(output,i-left+1)
                freq[str[left]]-=1
                if freq[str[left]]==0:
                    del freq[str[left]]
                left+=1
        return output
