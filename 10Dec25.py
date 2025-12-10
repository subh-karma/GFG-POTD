class Solution:
    def findTwoElement(self, arr):
        # code here
        ans = []
        for e in arr:
            i = abs(e)-1
            if arr[i] < 0:
                ans.append(abs(e)) 
            else:
                arr[i] *= -1
        
        for i, e in enumerate(arr):
            if e > 0:
                ans.append(i+1)
                break
        #print(arr)
        return ans
 

        # code here

