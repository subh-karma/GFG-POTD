class Solution:
    def celebrity(self, mat):
        # code here
        count = 0
        for item in mat:
            if item.count(1)==1: # if the count of row ==1 it means that the row is eligible for celebrity
                index = mat.index(item)
                count+=1
                break
        if count==0:
            return -1 # no celebrity
        for item in mat:
            if item[index]==0: # if someone does not know the eligible candidate, then return -1 
                return -1
        else: # otherwise return the eligible candidate
            return index
        # code here
        
